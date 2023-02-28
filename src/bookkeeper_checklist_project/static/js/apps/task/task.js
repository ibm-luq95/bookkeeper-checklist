"use strict";

import {
  sendRequest,
  fetchUrlPathByName,
  formInputSerializer,
  setFormInputValues,
} from "../../utils/helpers.js";
import { MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  //task:api:manager:create, task:api:manager:update
  const allCheckedTasks = new Array();
  const taskModalId = "tasks-form-modal";
  const taskModalElement = document.querySelector(`#${taskModalId}`);
  const taskModalFormElement = taskModalElement.querySelector("form");
  const taskModalFormFieldsetElement = taskModalFormElement.querySelector("fieldset");
  const taskModalTitleElement = taskModalElement.querySelector(".modal__title");
  const taskModalSubmitElement = taskModalElement.querySelector("button[type='submit']");
  const addTaskBtn = document.querySelector("button#addTaskBtn");

  const taskUpdateBtn = document.querySelectorAll(".taskUpdateBtn");
  const taskDeleteBtn = document.querySelectorAll(".taskDeleteBtn");
  const taskParentCheckboxInput = document.querySelector("input#taskParentCheckboxInput");
  const taskCheckboxInputs = document.querySelectorAll("input.taskCheckboxInput");
  const setTaskCompletedBtn = document.querySelector("button#setTaskCompletedBtn");

  // set task completed button
  if (setTaskCompletedBtn) {
    setTaskCompletedBtn.addEventListener("click", async (event) => {
      if (allCheckedTasks.length > 0) {
        const url = await fetchUrlPathByName("task:api:set-task-completed");
        const requestOptions = {
          method: "PUT",
          dataToSend: { tasks: allCheckedTasks },
          url: url["urlPath"],
        };
        setTaskCompletedBtn.setAttribute("disabled", "disabled");
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
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
            setTaskCompletedBtn.removeAttribute("disabled");
          });
      }
    });
  }

  // parent checkbox event
  if (taskParentCheckboxInput) {
    taskParentCheckboxInput.addEventListener("change", (ev) => {
      const checked = ev.currentTarget.checked;
      if (checked === true) {
        taskCheckboxInputs.forEach((input) => {
          input.checked = true;
        });
      } else {
        taskCheckboxInputs.forEach((input) => {
          input.checked = false;
        });
      }
      const changeEvent = new Event("change");
      taskCheckboxInputs.forEach((input) => {
        input.dispatchEvent(changeEvent);
      });
    });
  }

  taskCheckboxInputs.forEach((input) => {
    input.addEventListener("change", (event) => {
      const currentTarget = event.currentTarget;
      const taskId = currentTarget.value;
      if (event.currentTarget.checked === true) {
        allCheckedTasks.push(taskId);
      } else {
        const idx = allCheckedTasks.indexOf(taskId);
        // delete allCheckedTasks[idx];
        allCheckedTasks.splice(idx);
      }
      // console.log(allCheckedTasks);
    });
  });

  // show create new task modal
  // eslint-disable-next-line no-unused-vars
  if (addTaskBtn) {
    addTaskBtn.addEventListener("click", (event) => {
      const callBacks = {
        onOpenCallBack: async () => {
          taskModalTitleElement.textContent = "Create new task";
          taskModalSubmitElement.textContent = "Create";
          taskModalFormElement.setAttribute("method", "POST");
          taskModalFormElement["_method"].value = "POST";

          const createUrl = await fetchUrlPathByName("task:api:create");
          taskModalFormElement.setAttribute("action", createUrl["urlPath"]);
        },
        onCloseCallback: () => {
          taskModalFormElement["_method"].value = "";
        },
      };
      new MicroModalHandler(taskModalId, callBacks);
    });
  }

  // create new task form event
  taskModalFormElement.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    taskModalFormFieldsetElement.disabled = true;
    taskModalSubmitElement.disabled = true; // @audit
    taskModalSubmitElement.classList.add("is-disabled");
    Array.from(currentTarget.elements).forEach((element) => {
      element.classList.remove("is-danger");
    });
    const inputs = formInputSerializer({
      formElement: currentTarget,
      excludedFields: ["_method"],
      isOrdered: true,
    });
    inputs["created_by"] = currentTarget["user"].value;
    // console.log(inputs);
    // console.log(formData);
    const requestOptions = {
      method: currentTarget["_method"].value,
      dataToSend: inputs,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        showToastNotification(data["msg"], "success");
        setTimeout(() => {
          window.location.reload();
        }, 500);
      })
      .catch((error) => {
        console.error(error);
        showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        taskModalFormFieldsetElement.disabled = false;
        taskModalSubmitElement.disabled = false;
        const userErrors = error["user_error_msg"];
        for (const key in userErrors) {
          if (Object.hasOwnProperty.call(userErrors, key)) {
            const element = userErrors[key];
            currentTarget[key].classList.add(...["is-danger"]);
          }
        }
      });
  });

  // view task buttons
  if (taskUpdateBtn) {
    taskUpdateBtn.forEach((btn) => {
      btn.addEventListener("click", async (event) => {
        event.preventDefault();
        const taskId = event.currentTarget.dataset["itemId"];
        const retrieveUrl = await fetchUrlPathByName("task:api:retrieve");
        const updateUrl = await fetchUrlPathByName("task:api:update");
        const callBacks = {
          onOpenCallBack: () => {
            // console.log("Open update job");
            taskModalTitleElement.textContent = "Update task";
            taskModalSubmitElement.textContent = "Update";
            taskModalFormElement["_method"].value = "PUT";
            taskModalFormElement.setAttribute("action", updateUrl["urlPath"]);
            taskModalFormElement.setAttribute("method", "PUT");
            const requestOptions = {
              method: "POST",
              dataToSend: { taskId: taskId },
              url: retrieveUrl["urlPath"],
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const taskObject = data["task"];
                // console.log(taskObject);
                setFormInputValues(taskModalFormElement, taskObject);
                taskModalFormElement["id"].value = taskObject["id"];
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              })
              .finally(() => {
                // jobsFormFieldset.disabled = false;
                // managerJobsLoaderBtn.hidden = true;
              });
          },
          onCloseCallback: () => {
            console.warn("Close Update task");
            taskModalFormElement.reset();
          },
        };
        new MicroModalHandler(taskModalId, callBacks);
      });
    });
  }

  // delete task buttons
  if (taskDeleteBtn) {
    taskDeleteBtn.forEach((btn) => {
      btn.addEventListener("click", async (event) => {
        event.preventDefault();
        const taskId = event.currentTarget.dataset["itemId"];
        const taskTitle = event.currentTarget.dataset["taskTitle"];
        const deleteUrl = await fetchUrlPathByName("task:api:delete");
        const msg = confirm(`Do you want to delete task?`);
        if (msg) {
          const requestOptions = {
            method: "DELETE",
            dataToSend: { taskId: taskId },
            url: deleteUrl["urlPath"],
          };
          const request = sendRequest(requestOptions);
          request
            .then((data) => {
              console.log(data);
              showToastNotification(`${JSON.stringify(data["msg"])}`, "success");
              setTimeout(() => {
                window.location.reload();
              }, 500);
            })
            .catch((error) => {
              console.error(error);
              showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
            })
            .finally(() => {});
        }
      });
    });
  }
});
