"use strict";

import { convertStrToBool, fetchUrlPathByName, sendRequest } from "../../utils/helpers.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const editableContentsElements = document.querySelectorAll(".editable-content");
  const jobDetailsBookkeeperSelect = document.querySelector("select#jobDetailsBookkeeperSelect");
  const jobUpdateManagedByBtn = document.querySelector("button#jobUpdateManagedByBtn");
  const managedByCheckMark = document.querySelector("span#managedByCheckMark");
  const dueDateUpdateElement = document.querySelector("input#dueDateUpdateElement");
  const updateManagedByForm = document.querySelector("form#updateManagedByForm");
  const updateDueDateJobForm = document.querySelector("form#updateDueDateJobForm");
  const dueDateElement = document.querySelector("time#dueDateElement");
  const checkDueDateIcon = document.querySelector("i#checkDueDateIcon");

  if (editableContentsElements.length > 0) {
    editableContentsElements.forEach((element) => {
      element.addEventListener("dblclick", (event) => {
        const currentTarget = event.currentTarget;
        const isEditable = currentTarget.dataset["isEditable"];
        const isDate = convertStrToBool(currentTarget.dataset["isDate"]);
        if (isDate === false) {
          if (convertStrToBool(isEditable) === true) {
            const pk = currentTarget.dataset["pk"];
            const field = currentTarget.dataset["field"];
            const oldValue = currentTarget.textContent.trim();
            currentTarget.setAttribute("data-old-value", oldValue);
            currentTarget.contentEditable = true;

            element.addEventListener("focusout", async (event) => {
              const currentTarget = event.currentTarget;
              // currentTarget.classList.add("tmp-disabled");
              const isEditable = currentTarget.dataset["isEditable"];
              const oldValue = currentTarget.dataset["oldValue"];
              if (convertStrToBool(isEditable) === true) {
                const newValue = currentTarget.textContent.trim();
                if (oldValue !== newValue) {
                  const pk = currentTarget.dataset["pk"];
                  const field = currentTarget.dataset["field"];

                  currentTarget.contentEditable = false;
                  currentTarget.setAttribute("data-is-editable", "False");
                  const data = {
                    pk: pk,
                    field: field,
                    newValue: newValue,
                    isManagedBy: false,
                    newData: {
                      [field]: newValue,
                    },
                  };
                  const url = await fetchUrlPathByName("jobs:api:update-editable");
                  const requestOptions = {
                    method: "PUT",
                    dataToSend: data,
                    url: url["urlPath"],
                  };
                  const request = sendRequest(requestOptions);
                  request
                    .then((data) => {
                      showToastNotification(data["msg"], "success");
                      currentTarget.classList.add("tmp-disabled");
                      document.title = `Job - ${data["title"]}`;
                      // setTimeout(() => {
                      //   window.location.reload();
                      // }, 500);
                    })
                    .catch((error) => {
                      console.error(error);
                      showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
                    })
                    .finally(() => {
                      // currentTarget.contentEditable = true;
                      currentTarget.setAttribute("data-is-editable", "True");
                      currentTarget.setAttribute("data-old-value", "");
                    });
                }
              }
            });
          }
        } else {
          updateDueDateJobForm.classList.remove("d-none");
        }
      });
    });
  }
  if (updateDueDateJobForm) {
    updateDueDateJobForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      dueDateUpdateElement.classList.remove("is-danger");
      const value = dueDateUpdateElement.value;
      const fieldset = updateDueDateJobForm.querySelector("fieldset");
      const pk = dueDateUpdateElement.dataset["pk"];
      const field = dueDateUpdateElement.dataset["field"];
      const data = {
        pk: pk,
        field: field,
        newValue: value,
        isManagedBy: false,
        newData: {
          [field]: value,
        },
      };
      // console.log(data);
      fieldset.disabled = true;
      const url = await fetchUrlPathByName("jobs:api:update-editable");
      const requestOptions = {
        method: "PUT",
        dataToSend: data,
        url: url["urlPath"],
      };
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification(data["msg"], "success");
          // dueDateElement.textContent = data["due_date"];
          dueDateElement.datetime = data["due_date"];
          dueDateUpdateElement.value = null;
          // dueDateUpdateElement.value = data["due_date"];
          // console.log(data);
          // checkDueDateIcon.classList.remove("d-none");
          setTimeout(() => {
            // window.location.reload();
            updateDueDateJobForm.classList.add("d-none");
            // checkDueDateIcon.classList.add("d-none");
          }, 1000);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["error"])}`, "danger");
          dueDateUpdateElement.classList.add("is-danger");
        })
        .finally(() => {
          // currentTarget.contentEditable = true;
          fieldset.disabled = false;
        });
    });
  }

  let tmpSelectedManager;
  if (jobDetailsBookkeeperSelect) {
    jobDetailsBookkeeperSelect.addEventListener("focus", (event) => {
      const idx = jobDetailsBookkeeperSelect.selectedIndex;
      tmpSelectedManager = idx;
    });
  }

  if (updateManagedByForm) {
    updateManagedByForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const fieldset = updateManagedByForm.querySelector("fieldset");
      const selectedValue = jobDetailsBookkeeperSelect.value;
      const selectedText =
        jobDetailsBookkeeperSelect.options[
          jobDetailsBookkeeperSelect.selectedIndex
        ].textContent.trim();
      fieldset.disabled = true;
      const cfm = confirm(`Do you want to change the bookkeeper to ${selectedText}?`);
      if (cfm) {
        const pk = jobDetailsBookkeeperSelect.dataset["pk"];
        const data = {
          pk: pk,
          field: "managed_by",
          newValue: selectedValue,
          isManagedBy: true,
        };
        const url = await fetchUrlPathByName("jobs:api:update-editable");
        const requestOptions = {
          method: "PUT",
          dataToSend: data,
          url: url["urlPath"],
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification(data["msg"], "success");
            managedByCheckMark.hidden = false;
            jobDetailsBookkeeperSelect.classList.add("tmp-disabled");
            setTimeout(() => {
              managedByCheckMark.hidden = true;
            }, 3000);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            fieldset.disabled = false;
          });
      } else {
        fieldset.disabled = false;
        jobDetailsBookkeeperSelect.selectedIndex = tmpSelectedManager;
      }
    });
  }
});
