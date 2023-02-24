"use strict";
import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
import {
  enableInputsOnLoad,
  formInputSerializer,
  sendRequest,
  UploadFileRequest,
  setFormInputValues,
} from "../../utils/helpers.js";
import { getCookie } from "../../utils/cookie.js";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const managerAddReplyForm = document.querySelector("form#managerAddReplyForm");
  const updateSpecialAssignmentStatusForm = document.querySelector(
    "form#updateSpecialAssignmentStatusForm",
  );
  if (updateSpecialAssignmentStatusForm) {
    updateSpecialAssignmentStatusForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fieldset = currentTarget.querySelector("fieldset");
      fieldset.disabled = true;
      const formData = formInputSerializer({ formElement: currentTarget });
      const requestOptions = {
        method: "PUT",
        dataToSend: formData,
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
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  }

  if (managerAddReplyForm) {
    // add reply form event
    managerAddReplyForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fieldset = currentTarget.querySelector("fieldset");
      fieldset.disabled = true;
      const formData = formInputSerializer({
        formElement: currentTarget,
        excludedFields: ["attachment"],
        returnAsFormData: true,
      });
      const attachment = currentTarget["attachment"].files[0];
      if (attachment) {
        formData.append("attachment", attachment);
      }
      const uploadRequest = new UploadFileRequest(
        currentTarget.action,
        formData,
        getCookie("csrftoken"),
        "POST",
        false,
      );
      const request = uploadRequest.sendRequest();
      request
        .then((data) => {
          // console.log(data);
          showToastNotification(data, "success");
          setTimeout(() => {
            window.location.reload();
          }, 400);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification("Error while add new discussion!", "danger");
        })
        .finally(() => {
          fieldset.disabled = false;
        });
    });
  }
});
