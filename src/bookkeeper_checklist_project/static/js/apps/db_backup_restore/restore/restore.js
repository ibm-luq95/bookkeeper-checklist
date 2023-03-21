"use strict";

import { fetchUrlPathByName, sendRequest } from "../../../utils/helpers.js";
import { showToastNotification } from "../../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const restoreDbBtn = document.querySelector("button#restoreDbBtn");
  const restoreAlert = document.querySelector("#restoreAlert");

  if (restoreDbBtn) {
    restoreDbBtn.addEventListener("click", async (event) => {
      const objectPk = restoreDbBtn.dataset["objectPk"];
      const name = restoreDbBtn.dataset["name"];

      const msg = confirm(`Do you want to restore the backup ${name}?`);
      if (msg) {
        restoreDbBtn.disabled = true;
        const restoreUrl = await fetchUrlPathByName("db_backup_restore:restore:api-restore");
        const data = {
          pk: objectPk,
        };
        const requestOptions = {
          method: "POST",
          dataToSend: data,
          url: restoreUrl["urlPath"],
        };
        restoreAlert.hidden = false;
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
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {});
      }
    });
  }
});
