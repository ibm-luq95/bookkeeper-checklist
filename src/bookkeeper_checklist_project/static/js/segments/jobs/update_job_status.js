"use strict";

import { sendRequest } from "../../utils/helpers.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const formElement = document.querySelector("form#updateJobStatusForm");

  formElement.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
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
      .finally(() => {});
  });
});
