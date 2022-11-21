"use strict";
import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import { enableInputsOnLoad, sendRequest, UploadFileRequest } from "../../utils/helpers.js";
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
  const managerShowClientImportantContactBtn = document.querySelector(
    "button#managerShowClientImportantContactBtn",
  );
  const addDocumentFormWrapper = document.querySelector("div#addDocumentFormWrapper");
  const addDocumentForm = addDocumentFormWrapper.querySelector("form#addDocumentForm");
  const addNoteFormWrapper = document.querySelector("div#addNoteFormWrapper");
  const addNoteForm = addNoteFormWrapper.querySelector("form#addNoteForm");
  const managerAddDocumentBtn = document.querySelector("button#managerAddDocumentBtn");
  const managerAddNoteBtn = document.querySelector("button#managerAddNoteBtn");
  const managerViewNoteBtn = document.querySelectorAll("button.managerViewNoteBtn");
  const managerDeleteNoteBtn = document.querySelectorAll("button.managerDeleteNoteBtn");
  const retrieveNoteFormWrapper = document.querySelector("div#retrieveNoteFormWrapper");
  const retrieveNoteForm = retrieveNoteFormWrapper.querySelector("form#retrieveNoteForm");
  const retrieveNoteFieldset = retrieveNoteFormWrapper.querySelector("fieldset");
  const companyServicesFormWrapper = document.querySelector("div#companyServicesFormWrapper");
  const companyServiceForm = companyServicesFormWrapper.querySelector("form#companyServiceForm");
  const companyServiceFieldset = companyServicesFormWrapper.querySelector("fieldset");
  const managerAddCompanyServiceBtn = document.querySelector("button#managerAddCompanyServiceBtn");
  const managerCompanyServicesLoaderBtn = document.querySelector(
    "button#managerCompanyServicesLoaderBtn",
  );

  if (managerAddDocumentBtn) {
    managerAddDocumentBtn.addEventListener("click", (e) => {
      e.preventDefault();
      showMicroModal("document-form-modal");
    });
  }
  managerAddCompanyServiceBtn.addEventListener("click", (event) => {
    showMicroModal("company-services-form-modal");
  });
  managerShowClientImportantContactBtn.addEventListener("click", (ev) => {
    showMicroModal("important-contact-form-modal");
  });
  managerAddNoteBtn.addEventListener("click", (event) => {
    showMicroModal("notes-form-modal");
  });

  // add document form event
  addDocumentForm.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const currentTarget = addDocumentForm;
    const documentFile = currentTarget["id_document_file"].files[0];
    const formData = new FormData();
    // console.log(currentTarget.action);
    // console.log(currentTarget.elements);
    formData.append("title", currentTarget["id_title"].value);
    formData.append("document_section", currentTarget["id_document_section"].value);
    formData.append("client", currentTarget.querySelector("#client").value);
    formData.append("user", currentTarget.querySelector("#user").value);
    formData.append("document_file", documentFile);
    /* formData.forEach((formDataItem) => {
      console.log(formDataItem);
    }); */
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
      // contentType: "multipart/form-data",
    };
    const uploadRequest = new UploadFileRequest(
      addDocumentForm.action,
      formData,
      getCookie("csrftoken"),
      "POST",
      false,
    );
    const request = uploadRequest.sendRequest();
    request
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification("Error while add new document!", "danger");
      });
    // console.log();
    /* const request = sendRequest(requestOptions);
    request
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
      }); */
  });

  // add notes form submit form
  addNoteForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = addNoteForm;
    retrieveNoteFieldset.disabled = true;
    /* for (const input of currentTarget.elements) {
      console.log(input);
    } */
    const formData = {
      title: currentTarget["title"].value,
      body: currentTarget["body"].value,
      user: currentTarget["user"].value,
      note_section: currentTarget["note_section"].value,
      client: currentTarget["client"].value,
    };
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
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
      });
  });

  // view note item event
  managerViewNoteBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const noteId = data["noteId"];
      const url = window.localStorage.getItem("retrieveNoteUrl");
      const managerNoteLoaderBtn = document.querySelector("button#managerNoteLoaderBtn");
      // const fullUrl = window.localStorage.getItem("origin") + url;
      const fullUrl = window.location.origin + url;
      const requestOptions = {
        method: "POST",
        dataToSend: { noteId: noteId },
        url: fullUrl,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          const noteData = data["note"];
          managerNoteLoaderBtn.hidden = true;
          const callBacks = {
            onOpenCallBack: () => {
              retrieveNoteForm.elements["note_id"].value = noteData["id"];
              retrieveNoteForm.elements["title"].value = noteData["title"];
              retrieveNoteForm.elements["body"].value = noteData["body"];
              retrieveNoteForm.elements["client"].value = noteData["client"];
              retrieveNoteForm.elements["note_section"].value = noteData["note_section"];
            },
            onCloseCallback: () => {
              retrieveNoteForm.elements["title"].value = "";
              retrieveNoteForm.elements["body"].value = "";
              retrieveNoteForm.elements["client"].value = "";
              retrieveNoteForm.elements["note_section"].value = "";
            },
          };
          const modlaHandler = new MicroModalHandler("note-retrieve-modal", callBacks);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        });
    });
  });
  // delete note item
  managerDeleteNoteBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const data = currentTarget.dataset;
      const fullUrl = window.location.origin + window.localStorage.getItem("DeleteNoteUrl");
      const noteId = data["noteId"];
      const confirmMsg = confirm("Do you want to delete the note?");
      if (confirmMsg) {
        const requestOptions = {
          method: "DELETE",
          dataToSend: { noteId: noteId },
          url: fullUrl,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification("Note deleted", "success");
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

  // update note event
  retrieveNoteForm.addEventListener("submit", (event) => {
    event.preventDefault();
    //const fullUrl = window.location.origin + window.localStorage.getItem("UpdateNoteUrl");
    const fullUrl = event.currentTarget.action;
    managerNoteLoaderBtn.hidden = false;
    retrieveNoteFieldset.disabled = true;
    const updatedData = {
      id: retrieveNoteForm.elements["note_id"].value,
      title: retrieveNoteForm.elements["title"].value,
      body: retrieveNoteForm.elements["body"].value,
      note_section: retrieveNoteForm.elements["note_section"].value,
      client: retrieveNoteForm.elements["client"].value,
      user: retrieveNoteForm.elements["user"].value,
    };
    const requestOptions = {
      method: "PUT",
      dataToSend: updatedData,
      url: fullUrl,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification("Note updated", "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
      })
      .finally(() => {
        managerNoteLoaderBtn.hidden = true;
        retrieveNoteFieldset.disabled = false;
        console.warn("Finally");
      });
  });
  const clipboardJs = new ClipboardJS(".copyBtn");
  clipboardJs.on("success", (e) => {
    // console.info("Action:", e.action);
    // console.info("Text:", e.text);
    // console.info("Trigger:", e.trigger);
    e.clearSelection();
    const copiedText = e.text;
    const element = e.trigger;
    const textType = element.dataset["textType"];
    switch (textType) {
      case "username":
        showToastNotification(`Username ${copiedText} copied successfully`, "success");
        break;

      case "password":
        showToastNotification(`Password copied successfully`, "success");
        break;
      case "url":
        showToastNotification(`Url copied successfully`, "success");
        break;
    }
  });
  // add new company service form event
  companyServiceForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    companyServiceFieldset.disabled = true;
    managerCompanyServicesLoaderBtn.hidden = false;
    const formData = {
      service_name: currentTarget["service_name"].value,
      label: currentTarget["label"].value,
      email: currentTarget["email"].value,
      password: currentTarget["password"].value,
      client: currentTarget["client"].value,
      user: currentTarget["user"].value,
    };
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification("Service created successfully", "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
      })
      .finally(() => {
        companyServiceFieldset.disabled = false;
        managerCompanyServicesLoaderBtn.hidden = true;
      });
  });

  const allShowASPasswordBtns = document.querySelectorAll(".showASUPasswordBtn");
  allShowASPasswordBtns.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const visibilityStatus = Boolean(parseInt(currentTarget.dataset["visibilityStatus"]));
      const passwordInputId = currentTarget.dataset["passwordInput"];
      const passwordInputElement = document.querySelector(`#${passwordInputId}`);
      if (visibilityStatus === true) {
        currentTarget.innerHTML = eyeIconHTMLCode;
        currentTarget.dataset["visibilityStatus"] = 0;
        passwordInputElement.type = "password";
      } else {
        currentTarget.innerHTML = eyeSlashIconHTMLCode;
        currentTarget.dataset["visibilityStatus"] = 1;
        passwordInputElement.type = "text";
      }
    });
  });
});
