"use strict";

import { eyeIconHTMLCode, eyeSlashIconHTMLCode } from "../../utils/constants.js";
import { getCookie } from "../../utils/cookie.js";
import {
  sendRequest,
  fetchUrlPathByName,
  formInputSerializer,
  setFormInputValues,
  addTxtToClipboardWithNotification,
  UploadFileRequest,
} from "../../utils/helpers.js";
import { MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  //documents:api:delete
  const modalId = "document-form-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const documentForm = modalElement.querySelector("form");
  const fieldset = documentForm.querySelector("fieldset");
  const managerDocumentElements = document.querySelectorAll(".managerDocumentElement");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const managerDeleteDocumentBtn = document.querySelectorAll(".managerDeleteDocumentBtn");
  const managerAddDocumentBtn = document.querySelector("button#addDocumentBtn");

  // create document modal
  if (managerAddDocumentBtn) {
    managerAddDocumentBtn.addEventListener("click", (e) => {
      e.preventDefault();
      const callBacks = {
        onOpenCallBack: async () => {
          modalTitleElement.textContent = "Create document";
          submitButton.textContent = "Create";
          documentForm.setAttribute("method", "POST");
          documentForm["_method"].value = "POST";

          const createUrl = await fetchUrlPathByName("documents:api:create");
          documentForm.setAttribute("action", createUrl["urlPath"]);
        },
        onCloseCallback: () => {
          documentForm["_method"].value = "";
        },
      };
      new MicroModalHandler(modalId, callBacks);
    });
  }

  // create new document submit event
  documentForm.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const currentTarget = documentForm;
    const documentFile = currentTarget.querySelector("input[type=file]").files[0];
    // fieldset.disabled = true;
    const formData = new FormData();
    // console.log(currentTarget.action);
    // console.log(currentTarget["client"]);
    const formInputs = formInputSerializer({
      formElement: currentTarget,
      // isOrdered: true,
      excludedFields: ["document_file", "_method"],
      returnAsFormData: true,
    });
    formInputs.append("document_file", documentFile);

    const uploadRequest = new UploadFileRequest(
      currentTarget.action,
      formInputs,
      getCookie("csrftoken"),
      currentTarget["_method"].value,
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
      .finally(() => {});
  });

  // view document buttons
  if (managerDocumentElements) {
    managerDocumentElements.forEach((element) => {
      element.addEventListener("click", async (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const dataset = currentTarget.dataset;
        const documentId = dataset["documentId"];
        // const url = window.localStorage.getItem("RetrieveDocumentUrl");
        const url = await fetchUrlPathByName("documents:api:retrieve");
        const requestOptions = {
          method: "POST",
          dataToSend: { documentId: documentId },
          url: url["urlPath"],
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            // console.log(data);
            const callBacks = {
              onOpenCallBack: async () => {
                modalTitleElement.textContent = "Update document";
                submitButton.textContent = "Update";
                documentForm.setAttribute("method", "PUT");
                documentForm["_method"].value = "PUT";

                // const updateUrl = await fetchUrlPathByName(
                //   "documents:api:update"
                // );
                // documentForm.setAttribute("action", updateUrl["urlPath"]);
              },
              onCloseCallback: () => {
                // documentForm["_method"].value = "";
                documentForm.reset();
              },
            };
            new MicroModalHandler(modalId, callBacks);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            console.warn("Finally");
          });
      });
    });
  }

  // delete document buttons
  managerDeleteDocumentBtn.forEach((btn) => {
    btn.addEventListener("click", async (ev) => {
      const currentTarget = ev.currentTarget;
      const documentId = currentTarget.dataset["documentId"];
      const documentTitle = currentTarget.dataset["documentTitle"];
      const url = await fetchUrlPathByName("documents:api:delete");
      const msg = confirm(`Do you want to delete document ${documentTitle}?`);
      if (msg === true) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { documentId: documentId },
          url: url["urlPath"],
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification("Document deleted successfully", "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          });
      }
    });
  });
});
