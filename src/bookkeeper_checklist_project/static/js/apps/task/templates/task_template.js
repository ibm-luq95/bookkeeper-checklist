"use strict";

import { getCookie } from "../../../utils/cookie.js";
import { GenerateTagElement } from "../../../utils/generate_elements.js";
import { UploadFileRequest, fetchUrlPathByName, formInputSerializer, sendGetRequest } from "../../../utils/helpers.js";
import { MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const modalId = "task-template-details-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal-card-title");
  const modalBodyElement = modalElement.querySelector(".modal-card-body");
  const modalFooterElement = modalElement.querySelector(".modal-card-foot");
  const submitBtn = modalFooterElement.querySelector("button.submit-btn");
  //   const formElement = modalElement.querySelector("form");
  //   const fieldset = formElement.querySelector("fieldset");
  //   const submitButton = modalElement.querySelector("button[type='submit']");
  const showTaskTemplateDetailsBtns = document.querySelectorAll(
    "button.show-task-template-details-btn",
  );
  const addNewTaskTemplateBtn = document.querySelector("button#addNewTaskTemplateBtn");
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll(".task-template-trigger") || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);
    const taskPK = $trigger.dataset["taskPk"];

    $trigger.addEventListener("click", async () => {
      // task:api:templates:retrieve
      const retrieveUrl = await fetchUrlPathByName("task:api:templates:retrieve", taskPK);

      modalTitleElement.textContent = "Task";
      const requestOptions = {
        url: retrieveUrl["urlPath"],
      };
      const request = sendGetRequest(requestOptions);
      request
        .then((data) => {
          console.log(data);
          openModal($target);
          modalTitleElement.textContent = data["title"].slice(0, 35) + "...";
          submitBtn.style.display = "none";
          const titleElement = modalBodyElement.querySelector("p#taskTemplateTitle");
          titleElement.textContent = data["title"];
          const notesElements = modalBodyElement.querySelector("p#taskTemplateNotes");
          notesElements.textContent = data["notes"];
          const typeElement = modalBodyElement.querySelector("p#taskTemplateType");
          const typeTagElement = new GenerateTagElement({
            tagText: data["task_type_display"],
            elementSize: "is-medium",
          });
          typeElement.appendChild(typeTagElement.getGeneratedElement());
          const statusElement = modalBodyElement.querySelector("p#taskTemplateStatus");

          const statusTagElement = new GenerateTagElement({
            tagText: data["status_display"],
            elementSize: "is-medium",
          });
          statusElement.appendChild(statusTagElement.getGeneratedElement());

          const taskTemplateItemsWrapper = modalBodyElement.querySelector(
            "ul#taskTemplateItemsWrapper",
          );
          if (data["items"].length > 0) {
            for (const iterator of data["items"]) {
              const tempLiElement = document.createElement("li");
              tempLiElement.textContent = iterator["title"];
              taskTemplateItemsWrapper.appendChild(tempLiElement);
            }
          } else {
            const tempLiElement = document.createElement("li");
            tempLiElement.classList.add("has-text-danger");
            tempLiElement.textContent = "No task items!";
            taskTemplateItemsWrapper.appendChild(tempLiElement);
          }
          const taskTemplateAttachment = modalBodyElement.querySelector("a#taskTemplateAttachment");
          if (data["attachment"]) {
            taskTemplateAttachment.download = data["attachment"];
            taskTemplateAttachment.href = data["attachment"];
          } else {
          }
        })
        .catch((error) => {
          console.error(error);
          showToastNotification("Error while retrieve task template!", "danger");
        });
    });
  });

  // add new task template button event
  if (addNewTaskTemplateBtn) {
    addNewTaskTemplateBtn.addEventListener("click", (event) => {
      const modal = event.currentTarget.dataset.target;
      const target = document.getElementById(modal);
      openModal(target);
      document.querySelector("form#createTaskTemplateForm").addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const url = currentTarget.action;

        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method", "attachment"],
          returnAsFormData: true,
        });
        if (currentTarget["attachment"]) {
          const attachmentEle = currentTarget["attachment"].files[0];
          formInputs.append("attachment", attachmentEle);
        }
        const uploadRequest = new UploadFileRequest(
          url,
          formInputs,
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
              // window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification("Error while add new task template!", "danger");
          })
          .finally(() => {});
      });
    });
  }
});
