"use strict";

import {
  disableAndEnableFieldsetItems,
  fetchUrlPathByName,
  sendRequest,
} from "../../../utils/helpers.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const jobTemplateDetailsOptionsForm = document.querySelector(
    "form#jobTemplateDetailsOptionsForm",
  );
  const jobTemplateDetailsOptions = document.querySelector("select#jobTemplateDetailsOptions");
  const jobTemplateDetailsOptionsBtn = document.querySelector(
    "button#jobTemplateDetailsOptionsBtn",
  );
  const jobTemplateDetailsAlert = document.querySelector("div#jobTemplateDetailsAlert");
  const jobTemplateDetailsErrorAlert = document.querySelector("div#jobTemplateDetailsErrorAlert");
  const clientListForm = document.querySelector("form#clientListForm");

  // form submit event
  if (jobTemplateDetailsOptionsForm) {
    jobTemplateDetailsOptionsForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fieldset = currentTarget.querySelector("fieldset");
      if (jobTemplateDetailsOptions.value !== "") {
        const selectedOption =
          jobTemplateDetailsOptions.options[jobTemplateDetailsOptions.selectedIndex];
        const label = selectedOption.dataset["label"];
        const status = jobTemplateDetailsOptions.dataset["status"];
        const templatePk = jobTemplateDetailsOptions.dataset["templatePk"];
        const selectedValue = jobTemplateDetailsOptions.value;
        // const draftConfirm = confirm(
        //   "This template is in draft status, do you want to create new job from it?",
        // );
        switch (selectedValue) {
          case "create_job":
            jobTemplateDetailsAlert.textContent = `Please wait while ${label.toLowerCase()}`;
            jobTemplateDetailsAlert.hidden = false;
            fieldset.disabled = true;
            const data = {
              templatePk: templatePk,
              selectedOption: jobTemplateDetailsOptions.value,
              clients: [],
            };
            const url = await fetchUrlPathByName("jobs:api:templates:create-job-from-template");
            const requestOptions = {
              method: "POST",
              dataToSend: data,
              url: url["urlPath"],
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                showToastNotification(data["msg"], "success");
                console.log(data);
                setTimeout(() => {
                  // window.location.reload();
                  window.location.href = data["job_url"];
                }, 500);
              })
              .catch((error) => {
                console.error(error);
                jobTemplateDetailsErrorAlert.textContent = error.message;
                jobTemplateDetailsErrorAlert.hidden = false;
                // showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              })
              .finally(() => {
                fieldset.disabled = false;
              });
            break;

          case "create_job_for_multiple_clients":
            const myModal = new HystModal({
              linkAttributeName: "data-hystmodal",
              catchFocus: true,
              waitTransitions: true,
              closeOnEsc: false,
              beforeOpen: (modal) => {
                // console.log("Message before opening the modal");
                // console.log(modal); //modal window object
              },
              afterClose: (modal) => {
                // console.log("Message after modal has closed");
                // console.log(modal); //modal window object
              },
            });
            myModal.open("#client-list-form-modal");
            // console.log(myModal);
            break;

          default:
            break;
        }
      }
    });
  }

  // add clients form event
  if (clientListForm) {
    clientListForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const clientListLoader = document.querySelector("div#clientListLoader");
      const templateManager = document.querySelector("select#templateManager");
      const fieldset = document.querySelector("fieldset");
      const jobTemplatePk = clientListForm["job_template_pk"].value;
      const checked = clientListForm.querySelectorAll('input[type="checkbox"]:checked');
      // console.log(jobTemplatePk);
      // check if there checked clients
      if (checked.length > 0) {
        disableAndEnableFieldsetItems({ formElement: clientListForm, state: "disable" });
        clientListLoader.style.display = "inline-block";
        const checkedArrayValues = Array.from(checked).map((x) => x.value);
        const dataToSend = {
          templatePk: jobTemplatePk,
          clients: checkedArrayValues,
          selectedOption: "create_job_for_multiple_clients",
          templateManager: templateManager.value,
        };
        const url = await fetchUrlPathByName("jobs:api:templates:create-job-from-template");
        const requestOptions = {
          method: "POST",
          dataToSend: dataToSend,
          url: url["urlPath"],
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            showToastNotification(data["msg"], "success");
            console.log(data);
            setTimeout(() => {
              window.location.reload();
              // window.location.href = data["job_url"];
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            jobTemplateDetailsErrorAlert.textContent = error.message;
            jobTemplateDetailsErrorAlert.hidden = false;
            // showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            fieldset.disabled = false;
          });
      } else {
        clientListLoader.style.display = "none";
        showToastNotification("Please pick client from list!", "danger");
      }
    });
  }
});
