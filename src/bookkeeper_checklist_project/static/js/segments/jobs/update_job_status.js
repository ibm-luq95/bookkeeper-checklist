"use strict";

import { sendRequest } from "../../utils/helpers.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const formElement = document.querySelector("form#updateJobStatusForm");

  formElement.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const fieldset = currentTarget.querySelector("fieldset");
    fieldset.disabled = true;
    const status = currentTarget["status"].value;
    const jobId = currentTarget["jobId"].value;
    const formInputs = {
      jobId: jobId,
      status: status,
    };
    const requestOptions = {
      method: "PUT",
      dataToSend: formInputs,
      url: currentTarget.action,
    };
    const request = sendRequest(requestOptions);
    request
      .then((data) => {
        console.log(data);
        showToastNotification(data["msg"], "success");
        setTimeout(() => {
//          if (data["status"] === "completed" || data["status"] === "archived") {
//            const currentUrl = document.referrer;
//            window.location.href = currentUrl;
//            // history.go(-1);
//          } else {
//            window.location.reload();
//          }
           window.location.reload();
        }, 600);
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
