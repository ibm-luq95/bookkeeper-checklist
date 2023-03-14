"use strict";

import { formInputSerializer, sendRequest } from "../../../utils/helpers.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }
  const addTemplateNotesBtn = document.querySelector("button#addTemplateNotesBtn");
  const noteTemplateDeleteBtns = document.querySelectorAll(".note-template-delete-btn");
  if (addTemplateNotesBtn) {
    addTemplateNotesBtn.addEventListener("click", (event) => {
      const modal = event.currentTarget.dataset.target;
      const target = document.getElementById(modal);
      openModal(target);
      document.querySelector("form#createNoteTemplateForm").addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const fieldset = currentTarget.querySelector("fieldset");
        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method"],
        });
        fieldset.disabled = true;
        const jobTemplate = formInputs["job_template"];
        formInputs["job_template"] = [jobTemplate.value];
        console.log(formInputs);
        const requestOptions = {
          method: currentTarget.method,
          dataToSend: formInputs,
          url: currentTarget.action,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            showToastNotification(data["msg"], "success");
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
  }

  // noteTemplateDeleteBtns
  if (noteTemplateDeleteBtns) {
    noteTemplateDeleteBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
      });
    });
  }
});
