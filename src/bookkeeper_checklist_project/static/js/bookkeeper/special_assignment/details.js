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
  const bookkeeperAddReplyForm = document.querySelector(
    "form#bookkeeperAddReplyForm"
  );
  const updateSpecialAssignmentStatusForm = document.querySelector(
    "form#updateSpecialAssignmentStatusForm"
  );

  updateSpecialAssignmentStatusForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const fieldset = currentTarget.querySelector("fieldset");
    fieldset.disabled = true;
    const formData = formInputSerializer({formElement: currentTarget});
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
        showToastNotification(
          `${JSON.stringify(error["user_error_msg"])}`,
          "danger"
        );
      })
      .finally(() => {
        fieldset.disabled = false;
      });
  });
  // add reply form event
  bookkeeperAddReplyForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const currentTarget = event.currentTarget;
    const fieldset = currentTarget.querySelector("fieldset");
    fieldset.disabled = true;
    const inputs = formInputSerializer({formElement: currentTarget});
    const formData = new FormData();
    // Array.from(currentTarget.elements).forEach(ele => {
    //   console.log(ele);
    // });
    const attachment = currentTarget["attachment"].files[0];
    if (attachment) {
      //   console.log(attachment);
      formData.append("attachment", attachment);
    }
    formData.append("body", currentTarget["body"].value);
    formData.append(
      "special_assignment",
      currentTarget["special_assignment"].value
    );
    formData.append("title", currentTarget["title"].value);
    formData.append("bookkeeper", currentTarget["bookkeeper"].value);

    if (currentTarget["replies"].value) {
      formData.append("replies", currentTarget["replies"].value);
    }

    // formData.append("replies", 0);
    const requestOptions = {
      method: "POST",
      dataToSend: formData,
      url: currentTarget.action,
    };
    // console.table(Object.fromEntries(formData));
    // console.log(Object.fromEntries(formData));
    // throw new Error("pause");
    // formData.append("special_assignment_id", inputs["special_assignment"]);
    const uploadRequest = new UploadFileRequest(
      currentTarget.action,
      formData,
      getCookie("csrftoken"),
      "POST",
      false
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
        showToastNotification("Error while add new discussion!", "danger");
      })
      .finally(() => {
        fieldset.disabled = false;
      });
  });
});
