"use strict";

import { DataTableHelper } from "../../../utils/datatable-helper.js";
import {
  formInputSerializer,
  sendRequest,
  setFormInputValues,
} from "../../../utils/helpers.js";
import { MicroModalHandler } from "../../../utils/model-box.js";
import { showToastNotification } from "../../../utils/notifications.js";
document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const taskModalID = "tasks-form-modal";
  const taskModalElement = document.querySelector(`#${taskModalID}`);
  const taskModalTitleElement = taskModalElement.querySelector(".modal__title");
  const taskModalSubmitBtn = taskModalElement.querySelector(
    "button[type='submit']"
  );
  const taskModalForm = taskModalElement.querySelector(`form`);
  const bookkeeperTaskCheckboxInputs = document.querySelectorAll(
    "input.bookkeeperTaskCheckboxInput"
  );
  const bookkeeperTaskParentCheckboxInput = document.querySelector(
    "input#bookkeeperTaskParentCheckboxInput"
  );
  const taskViewBtns = document.querySelectorAll(".taskViewBtn");
  const taskDeleteBtns = document.querySelectorAll(".taskDeleteBtn");

  const allCheckedTasks = new Array();
  const bookkeeperAddTaskBtn = document.querySelector(
    "button#bookkeeperAddTaskBtn"
  );

  // task checkbox items
  bookkeeperTaskCheckboxInputs.forEach((input) => {
    input.addEventListener("change", (event) => {
      const currentTarget = event.currentTarget;

      const taskId = currentTarget.value;
      if (event.currentTarget.checked === true) {
        allCheckedTasks.push(taskId);
      } else {
        const idx = allCheckedTasks.indexOf(taskId);
        // delete allCheckedTasks[idx];
        allCheckedTasks.splice(idx, 1);
      }
    });
  });
  if (bookkeeperTaskParentCheckboxInput) {
    bookkeeperTaskParentCheckboxInput.addEventListener("change", (ev) => {
      const checked = ev.currentTarget.checked;
      if (checked === true) {
        bookkeeperTaskCheckboxInputs.forEach((input) => {
          input.checked = true;
        });
      } else {
        bookkeeperTaskCheckboxInputs.forEach((input) => {
          input.checked = false;
        });
      }
      const changeEvent = new Event("change");
      bookkeeperTaskCheckboxInputs.forEach((input) => {
        input.dispatchEvent(changeEvent);
      });
    });
  }

  // task delete buttons
  if (taskDeleteBtns) {
    taskDeleteBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const taskId = currentTarget.dataset["taskId"];
        const taskTitle = currentTarget.dataset["taskTitle"];
        const confirmMsg = confirm(`Do you want to delete task ${taskTitle}`);
        if (confirmMsg) {
          const requestOptions = {
            method: "DELETE",
            dataToSend: { taskId: taskId },
            url: window.localStorage.getItem("BookkeeperTasksApiDeleteUrl"),
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
              showToastNotification(
                `${JSON.stringify(error["user_error_msg"])}`,
                "danger"
              );
            });
        }
      });
    });
  }
  // init data table for tasks table
  if (document.querySelector("table#bookkeeperJobTasksTable")) {
    new DataTableHelper({
      tableID: "bookkeeperJobTasksTable",
      buttons: [
        {
          text: "Done",
          action: (e, dt, node, config) => {
            // @audit
            if (allCheckedTasks.length <= 0) {
              alert("No tasks checked");
            } else {
              const requestOptions = {
                method: "PUT",
                dataToSend: { tasks: allCheckedTasks },
                url: window.localStorage.getItem("BookkeeperTaskCompletedUrl"),
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
                  showToastNotification(
                    `${JSON.stringify(error["user_error_msg"])}`,
                    "danger"
                  );
                });
            }
          },
        },
        "csv",
        "pdf",
      ],
    });
  }

  // add task button
  bookkeeperAddTaskBtn.addEventListener("click", (event) => {
    const callBacks = {
      onOpenCallBack: () => {
        taskModalForm.reset();
        taskModalTitleElement.textContent = "Create new task";
        taskModalSubmitBtn.textContent = "Create";
        taskModalSubmitBtn.hidden = false;
        taskModalForm.elements["_method"].value = "POST";
        taskModalForm.setAttribute(
          "action",
          window.localStorage.getItem("BookkeeperTasksApiCreateUrl")
        );
      },
      onCloseCallback: () => {
        taskModalSubmitBtn.disabled = false;
      },
    };
    const modalHandler = new MicroModalHandler(taskModalID, callBacks);
  });

  // view task buttons
  if (taskViewBtns) {
    taskViewBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const isOwner = Boolean(parseInt(currentTarget.dataset["owner"]));
        const taskId = currentTarget.dataset["taskId"];

        const callBacks = {
          onOpenCallBack: () => {
            taskModalTitleElement.textContent = "Update task";
            taskModalSubmitBtn.textContent = "Update";
            taskModalSubmitBtn.hidden = false;
            taskModalForm.elements["_method"].value = "PUT";
            taskModalForm.setAttribute(
              "action",
              window.localStorage.getItem("BookkeeperTasksApiUpdateUrl")
            );

            // check if task belong to current bookkeeper
            if (isOwner === true) {
              taskModalSubmitBtn.hidden = false;
            } else {
              taskModalSubmitBtn.hidden = true;
            }

            const requestOptions = {
              method: "POST",
              dataToSend: { taskId: taskId },
              url: window.localStorage.getItem("BookkeeperTasksApiRetrieveUrl"),
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const taskData = data["task"];
                setFormInputValues(taskModalForm, taskData);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(
                  `${JSON.stringify(error["user_error_msg"])}`,
                  "danger"
                );
              });
          },
          onCloseCallback: () => {
            taskModalSubmitBtn.disabled = false;
          },
        };
        const modalHandler = new MicroModalHandler(taskModalID, callBacks);
      });
    });
  }

  // add new task form submit
  if (taskModalForm) {
    taskModalForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fieldset = currentTarget.querySelector("fieldset");
      const formInputs = formInputSerializer(currentTarget);
      fieldset.disabled = true;
      taskModalSubmitBtn.disabled = true;
      const requestOptions = {
        method: currentTarget.elements["_method"].value,
        dataToSend: formInputs,
        url: currentTarget.action,
      };
      console.log(requestOptions);
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
          showToastNotification(
            `${JSON.stringify(error["user_error_msg"])}`,
            "danger"
          );
        })
        .finally(() => {
          fieldset.disabled = false;
          taskModalSubmitBtn.disabled = false;
        });
    });
  }
});
