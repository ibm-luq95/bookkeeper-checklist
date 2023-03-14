"use strict";

import { fetchUrlPathByName, formInputSerializer, sendRequest } from "../../../utils/helpers.js";
import { MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const modalId = "template-task-item-modal";
  const modalElement = document.querySelector(`#${modalId}`);
  const modalTitleElement = modalElement.querySelector(".modal__title");
  const formElement = modalElement.querySelector("form");
  const fieldset = formElement.querySelector("fieldset");
  const submitButton = modalElement.querySelector("button[type='submit']");
  const addNewTaskItemBtns = document.querySelectorAll("button.add-new-task-item-btn");
  const deleteTaskTemplateBtns = document.querySelectorAll("button.delete-task-template-btn");

  const taskTemplateItems = document.querySelectorAll("a.task-template-item");
  const taskItemsUlWrapper = document.querySelector("ul#task-items-ul-wrapper");

  // add task item to task
  if (addNewTaskItemBtns) {
    addNewTaskItemBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const taskPk = currentTarget.dataset["taskPk"];
        const callBacks = {
          onOpenCallBack: async () => {
            modalTitleElement.textContent = "Create new task item";
            submitButton.textContent = "Create";
            formElement.setAttribute("method", "POST");
            formElement["_method"].value = "POST";
            formElement["task"].value = taskPk;

            const createUrl = await fetchUrlPathByName("task:api:templates:create-task-item");
            formElement.setAttribute("action", createUrl["urlPath"]);
          },
          onCloseCallback: () => {
            formElement["_method"].value = "";
          },
        };
        new MicroModalHandler(modalId, callBacks);
      });
    });
  }

  // task item form submit event
  if (formElement) {
    formElement.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      fieldset.disabled = true;
      const url = currentTarget.action;
      const formInputs = formInputSerializer({
        formElement: currentTarget,
        excludedFields: ["_method"],
      });
      const requestOptions = {
        method: currentTarget["_method"].value,
        dataToSend: formInputs,
        url: url,
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification(data["msg"], "success");
          MicroModal.close(modalId);
          const newTaskItem = data["taskItem"];
          //taskItemsUlWrapper
          const tmpNewLiElement = document.createElement("li");
          const tmpNewAElement = document.createElement("a");
          tmpNewAElement.textContent = newTaskItem["title"].slice(0, 25);
          tmpNewAElement.classList.add(...["task-template-item", "font-size-13px"]);
          tmpNewAElement.setAttribute("data-element-pk", newTaskItem["pk"]);
          tmpNewAElement.setAttribute("data-task-parent-pk", newTaskItem["taskParentPK"]);
          tmpNewLiElement.appendChild(tmpNewAElement);
          taskItemsUlWrapper.appendChild(tmpNewLiElement);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  }

  // task template items
  if (taskTemplateItems) {
    taskTemplateItems.forEach((element) => {
      element.addEventListener("click", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
      });
    });
  }

  // task template delete buttons
  if (deleteTaskTemplateBtns) {
    deleteTaskTemplateBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        event.preventDefault();
        //task:api:templates:delete
        const currentTarget = event.currentTarget;
        const taskPk = currentTarget.dataset["taskPk"];
        const msg = confirm("Do you want to delete task template?");
        if (msg) {
          const deleteUrl = fetchUrlPathByName("task:api:templates:delete", taskPk);
          deleteUrl.then((data) => {
            const url = data["urlPath"];
            const requestOptions = {
              method: "DELETE",
              url: url,
            };
            const request = sendRequest(requestOptions);
            request
              .then((requestData) => {
                console.log(requestData);
              })
              .catch((error) => {
                console.error(error);
                // showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              });
          });
        }
      });
    });
  }
});
