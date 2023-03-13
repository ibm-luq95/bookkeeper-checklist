"use strict";

import { getCookie } from "../../../utils/cookie.js";
import { UploadFileRequest } from "../../../utils/helpers.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const addTemplateDocumentBtn = document.querySelector("button#addTemplateDocumentBtn");
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }
  if (addTemplateDocumentBtn) {
    addTemplateDocumentBtn.addEventListener("click", (event) => {
      event.preventDefault();
      const modal = event.currentTarget.dataset.target;
      const target = document.getElementById(modal);
      openModal(target);
      document
        .querySelector("form#createDocumentTemplateForm")
        .addEventListener("submit", (event) => {
          event.preventDefault();
          const currentTarget = event.currentTarget;
          const url = currentTarget.action;
          const formData = new FormData();
          formData.append("title", currentTarget["title"].value);
          formData.append("template_file", currentTarget["template_file"].files[0]);
          const uploadRequest = new UploadFileRequest(
            url,
            formData,
            getCookie("csrftoken"),
            currentTarget.method,
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
              showToastNotification("Error while add new document template!", "danger");
            })
            .finally(() => {});
        });
    });
  }
});
