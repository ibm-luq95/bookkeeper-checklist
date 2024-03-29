"use strict";

/**
 * This will display notification message
 * @param {string} msg the message in the notification
 * @param {string} notificationType notification message type
 */
const showToastNotification = (msg, notificationType = "success") => {
  let color;
  if (notificationType === "success") {
    color = "#009688";
  } else if (notificationType === "danger" || notificationType === "error") {
    color = "#FF3860";
  } else if (notificationType === "warn") {
    color = "#FFDD57";
  }
  Toastify({
    text: msg,
    duration: 3000,
    // destination: "https://github.com/apvarun/toastify-js",
    // newWindow: true,
    close: true,
    gravity: "top",
    position: "right",
    stopOnFocus: true,
    style: {
      background: color,
    },
    onClick: function () {}, // Callback after click
  }).showToast();
};

export { showToastNotification };
