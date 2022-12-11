"use strict";

import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import {
  enableInputsOnLoad,
  formInputSerializer,
  sendRequest,
  UploadFileRequest,
} from "../../utils/helpers.js";
import { getCookie } from "../../utils/cookie.js";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const managerAddTaskBtn = document.querySelector("button#managerAddTaskBtn");
  const taskViewBtn = document.querySelectorAll("button.taskViewBtn");
  const taskDeleteBtn = document.querySelectorAll("button.taskDeleteBtn");
  const managerAddNoteToJobBtn = document.querySelector("button#managerAddNoteToJobBtn");
  const managerAddDocumentToJobBtn = document.querySelector("button#managerAddDocumentToJobBtn");
  const clientsTable = $("#managerJobTasksTable").DataTable({
    autoWidth: true,
    processing: true,
    // "info": false,
    // "paging": false,
    // stateSave: true,
    stateSaveCallback: function (settings, data) {
      localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
    },
    stateLoadCallback: function (settings) {
      return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
    },
    fixedHeader: true,
    responsive: true,
    dom: "Bfrtip",
    buttons: [
      // "copy",
      "csv",
      "pdf",
    ],
  });

  managerAddTaskBtn.addEventListener("click", (ev) => {
    showMicroModal("tasks-form-modal");
  });

  taskViewBtn.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
      const currentTarget = ev.currentTarget;
      const taskId = currentTarget.dataset["taskId"];
      alert(taskId);
    });
  });
  taskDeleteBtn.forEach((btn) => {
    btn.addEventListener("click", (ev) => {
      const currentTarget = ev.currentTarget;
      const taskId = currentTarget.dataset["taskId"];
      alert(taskId);
    });
  });

  // add note button event
  managerAddNoteToJobBtn.addEventListener("click", (event) => {
    // @follow-up
    const callBacks = {
      onOpenCallBack: () => {},
      onCloseCallback: () => {},
    };
    const modlaHandler = new MicroModalHandler("note-form-modal", callBacks);
    const managerAddNewNoteForm = document.querySelector("form#managerAddNewNoteForm");
    const fieldset = managerAddNewNoteForm.querySelector("fieldset");

    managerAddNewNoteForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const formElements = formInputSerializer(currentTarget);
      fieldset.disabled = true;
      // console.log(formElements);
      // throw new Error("s");
      const requestOptions = {
        method: "POST",
        dataToSend: formElements,
        url: currentTarget.action,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification("Note created successfully", "success");
          setTimeout(() => {
            window.location.reload();
          }, 500);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  });

  // add document button event
  managerAddDocumentToJobBtn.addEventListener("click", (event) => {
    // @follow-up
    const callBacks = {
      onOpenCallBack: () => {},
      onCloseCallback: () => {},
    };
    const modlaHandler = new MicroModalHandler("document-form-modal", callBacks);
    const managerAddNewDocumentForm = document.querySelector("form#managerAddNewDocumentForm");
    const fieldset = managerAddNewDocumentForm.querySelector("fieldset");

    managerAddNewDocumentForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const documentFile = currentTarget["id_document_file"].files[0];
      fieldset.disabled = true;
      const formData = new FormData();
      // console.log(currentTarget.action);
      // console.log(currentTarget.elements);
      formData.append("title", currentTarget["id_title"].value);
      formData.append("document_section", currentTarget["id_document_section"].value);
      formData.append("client", currentTarget["client"].value);
      formData.append("user", currentTarget["user"].value);
      formData.append("job", currentTarget["job"].value);
      formData.append("document_file", documentFile);
      const requestOptions = {
        method: "POST",
        dataToSend: formData,
        url: currentTarget.action,
      };
      const uploadRequest = new UploadFileRequest(
        currentTarget.action,
        formData,
        getCookie("csrftoken"),
        "POST",
        false,
      );
      const request = uploadRequest.sendRequest();
      request
        .then((data) => {
          console.log(data);
          showToastNotification(data, "success");
          setTimeout(() => {
            window.location.reload();
          }, 500);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification("Error while add new document!", "danger");
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  });
});
