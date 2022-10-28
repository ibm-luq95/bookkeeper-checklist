"use strict";

import { isDisabledCssClass } from "./constants.js";
import { getCookie } from "./cookie.js";

const enableInputsOnLoad = (inputClassName) => {
  const allBkChLstInputs = document.querySelectorAll(`.${inputClassName}`);
  allBkChLstInputs.forEach((element) => {
    const isDisabled = element.dataset["isDisabled"];
    if (isDisabled !== "1") {
      element.disabled = false;
      element.classList.remove(isDisabledCssClass);
    }
  });
};
// fadeOut a dom element
const fadeOut = (el) => {
  el.style.opacity = 1;

  (function fade() {
    if ((el.style.opacity -= 0.1) < 0) {
      el.style.display = "none";
    } else {
      requestAnimationFrame(fade);
    }
  })();
};

// fadeIn a dom element
const fadeIn = (el, display) => {
  el.style.opacity = 0;
  el.style.display = display || "block";

  (function fade() {
    const val = parseFloat(el.style.opacity);
    if (!((val += 0.1) > 1)) {
      el.style.opacity = val;
      requestAnimationFrame(fade);
    }
  })();
};

const sendRequest = (options) => {
  return new Promise((resolve, reject) => {
    try {
      const url = options["url"];
      const controller = new AbortController(); // the AbortController
      const { signal } = controller;
      const headers = new Headers({
        "Content-Type": "application/json;charset=utf-8",
        // "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"] ? options["token"] : getCookie("csrftoken"),
      });
      const formData = Object.fromEntries(options["dataToSend"].entries());
      const fetchOptions = {
        method: options["method"],
        mode: "same-origin",
        credentials: "include",
        body: JSON.stringify(formData)
      };
      const request = new Request(url, {
        headers: headers,
        signal: signal,
      });
      const fetchObj = fetch(request, fetchOptions);
      fetchObj
        .then((response) => {
          if (!response.ok) {
            return response.text().then((text) => {
              reject(JSON.parse(text));
            });
          }
          resolve(response.json());
        })
        .catch((error) => {
          reject(error);
        });
    } catch (error) {
      reject(error);
    }
  });
};

export { enableInputsOnLoad, sendRequest, fadeIn, fadeOut };
