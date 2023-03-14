"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const jobTemplateDetailsOptions = document.querySelector("select#jobTemplateDetailsOptions");

  if (jobTemplateDetailsOptions) {
    jobTemplateDetailsOptions.addEventListener("change", (event) => {
      const currentTarget = event.currentTarget;
      alert(currentTarget.value);
    });
  }
});
