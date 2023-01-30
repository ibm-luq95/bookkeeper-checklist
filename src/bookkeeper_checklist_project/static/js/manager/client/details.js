"use strict";
import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import {
  enableInputsOnLoad,
  formInputSerializer,
  sendRequest,
  UploadFileRequest,
  setFormInputValues,
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
  /* const managerShowClientImportantContactBtn = document.querySelector(
    "button#managerShowClientImportantContactBtn",
  ); */







  const managerViewImportantContactBtns = document.querySelectorAll(
    "button.managerViewImportantContactBtn",
  );


  // const updateImportantContactForm = document.querySelector("form#updateImportantContactForm");

  // retrive important contact button event
  if (managerViewImportantContactBtns) {
    managerViewImportantContactBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const importantContactId = currentTarget.dataset["importantContactId"];
        const url = window.localStorage.getItem("RetrieveImportantContactUrl");
        const callBacks = {
          onOpenCallBack: () => {
            const requestOptions = {
              method: "POST",
              dataToSend: { importantContactId: importantContactId },
              url: url,
            };
            //updateImportantContactForm
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const importantContactObject = data["important_contact"];
                setFormInputValues(updateImportantContactForm, importantContactObject);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              })
              .finally(() => {
                // console.warn("Finally");
              });
          },
          onCloseCallback: () => {},
        };
        new MicroModalHandler("important-contact-form-modal", callBacks);
      });
    });
  }

  // update important contact form
  /* updateImportantContactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const fieldset = updateImportantContactForm.querySelector("fieldset");
    const formData = formInputSerializer({formElement: currentTarget});
    fieldset.disabled = true;
    const requestOptions = {
      method: "PUT",
      dataToSend: formData,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        console.log(data);
        showToastNotification("Important contact updated!", "success");
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
        console.warn("Finally");
      });
  }); */





  /* managerShowClientImportantContactBtn.addEventListener("click", (ev) => {
    showMicroModal("important-contact-form-modal");
  }); */


  // add document form event


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















});
