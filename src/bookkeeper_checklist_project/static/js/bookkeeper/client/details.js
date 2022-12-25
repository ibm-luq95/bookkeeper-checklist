"use strict";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";
import { showMicroModal, MicroModalHandler } from "../../utils/model-box.js";
import { enableInputsOnLoad, sendRequest, sendGetRequest, setFormInputValues } from "../../utils/helpers.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  if (document.readyState === "loading") {
  }

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  if (document.readyState === "interactive") {
  }

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    const clipboardJs = new ClipboardJS(".copyBtn");

    // first enable all bkchlst inputs when page fully loaded completed
    const inputTrimWhitespaceBtns = document.querySelectorAll(".input-trim-whitespace");

    inputTrimWhitespaceBtns.forEach((element) => {
      element.value = element.value.trim();
    });
    // Then instantiate the MicroModal module, so that it takes care of all the bindings for you.
    MicroModal.init({
      disableScroll: false,
    });

    const weeklyTasksInputs = document.querySelectorAll(".monthly-task-checkbox");
    const weeklyTasksSubmitBtn = document.querySelector("#weeklyTasksSubmitBtn");
    const updateTaskBookkeeperBtn = document.querySelector("button#updateTaskBookkeeperBtn");
    const bookkeeperViewImportantContactBtns = document.querySelectorAll(
      "button.bookkeeperViewImportantContactBtn",
    );

    // bookkeeper view important contact buttons event
    bookkeeperViewImportantContactBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const importantContactId = currentTarget.dataset["importantContactId"];
        const url = window.localStorage.getItem("RetrieveImportantContactUrl");
        const callBacks = {
          onOpenCallBack: () => {
            const requestOptions = {
              method: "POST",
              dataToSend: { importantContactId: importantContactId },
              url: url,
            };
            //updateImportantContactForm
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const importantContactObject = data["important_contact"];
                setFormInputValues(updateImportantContactForm, importantContactObject);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              })
              .finally(() => {
                // console.warn("Finally");
              });
          },
          onCloseCallback: () => {},
        };

        new MicroModalHandler("important-contact-form-modal", callBacks);
      });
    });

    // bookkeeper add new task button
    const bookkeeperAddNewTaskBtn = document.querySelector("#bookkeeperAddNewTaskBtn");
    bookkeeperAddNewTaskBtn.addEventListener("click", (event) => {
      MicroModal.show("add-new-task-modal", {
        disableScroll: false,
        onClose: (modal) => {
          console.info(`${modal.id} is hidden`);
        },
        disableFocus: false,
      });
    });

    // task items buttons
    const openTasksItemsModalBtns = document.querySelectorAll(".open-tasks-items-modal-btn");
    openTasksItemsModalBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        const noTasksNotification = document.querySelector("div#noTasksNotification");
        const tasksTableWrapper = document.querySelector("div#tasksTableWrapper");
        const currentTarget = event.currentTarget;
        const fetchJobUrl = window.localStorage.getItem("fetchJobsUrl");
        const jobId = currentTarget.dataset["jobId"];
        const tasksItemsModalTitle = document.querySelector("h2#tasks-items-modal-title");

        const callBacks = {
          onOpenCallBack: () => {
            const requestOptions = {
              method: "POST",
              dataToSend: { jobId: jobId },
              url: fetchJobUrl,
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                const jobObject = data["job"];

                tasksItemsModalTitle.textContent = jobObject["title"];
                const tasksArray = data["job"]["tasks"];

                // check if the tasks length
                if (tasksArray.length <= 0) {
                  noTasksNotification.hidden = false;
                  tasksTableWrapper.hidden = true;
                } else {
                  const jobTasksTable = document.querySelector("table#jobTasksTable");
                  tasksTableWrapper.hidden = false;
                  // console.log(data);
                  // console.log(tasksArray);

                  const tasksModalWrapperItems = document.querySelector(
                    "div#tasksModalWrapperItems",
                  );
                  const tableBody = jobTasksTable.querySelector("tbody");
                  tasksArray.forEach((taskElement) => {
                    const tableRaw = document.createElement("tr");
                    tableRaw.setAttribute("data-task-id", taskElement["id"]);
                    const tdCheckboxEle = document.createElement("td");
                    tdCheckboxEle.setAttribute("data-td-name", "task-td-checkbox");
                    const checkboxElement = document.createElement("input");
                    checkboxElement.type = "checkbox";
                    checkboxElement.classList.add("tasks-checkbox");
                    checkboxElement.setAttribute("data-task-id", taskElement["id"]);
                    // append check box to td
                    tdCheckboxEle.appendChild(checkboxElement);

                    // task title item
                    const tdTaskTitleTd = document.createElement("td");
                    tdTaskTitleTd.setAttribute("data-td-name", "task-td-title");
                    tdTaskTitleTd.textContent = taskElement["title"].substring(0, 15) + "...";
                    if (taskElement["is_completed"] === true) {
                      tdTaskTitleTd.classList.add("completed-task-item");
                      checkboxElement.checked = true;
                      checkboxElement.disabled = true;
                      tableRaw.classList.add("has-background-grey-lighter");
                      checkboxElement.setAttribute("data-set-disabled", "1");
                      checkboxElement.setAttribute("data-is-completed", "1");
                    }

                    // task status item
                    const tdTaskTypeTd = document.createElement("td");
                    tdTaskTypeTd.setAttribute("data-td-name", "task-td-status");
                    tdTaskTypeTd.textContent = taskElement["task_type"];

                    // task created at
                    const taskCreatedAtTd = document.createElement("td");
                    taskCreatedAtTd.setAttribute("data-td-name", "task-td-created-at");
                    taskCreatedAtTd.textContent = taskElement["created_at"];

                    // task due date
                    const taskDueDateTd = document.createElement("td");
                    taskDueDateTd.setAttribute("data-td-name", "task-td-due-date");
                    taskDueDateTd.textContent = taskElement["due_date"];

                    // console.log(taskElement["is_completed"]);
                    // task buttons td
                    const taskButtonsActionsTd = document.createElement("td");
                    taskButtonsActionsTd.setAttribute("data-td-name", "task-td-actions");
                    taskButtonsActionsTd.classList.add(...["is-actions-cell"]);
                    const divButtonsElement = document.createElement("div");
                    divButtonsElement.classList.add(...["buttons", "is-right"]);
                    const viewButton = document.createElement("button");
                    viewButton.type = "button";
                    viewButton.classList.add(
                      ...[
                        "button",
                        "is-small",
                        // "is-info",
                        "bkchlst-input",
                        "bookkeeperTaskViewBtn",
                      ],
                    );
                    viewButton.setAttribute("data-task-id", taskElement["id"]);
                    viewButton.setAttribute("data-tooltip", "View task");
                    const spanIconElement = document.createElement("span");
                    spanIconElement.classList.add("icon");
                    spanIconElement.innerHTML = '<i class="fa-solid fa-eye"></i>';
                    viewButton.appendChild(spanIconElement);
                    // append button to div buttons
                    divButtonsElement.appendChild(viewButton);
                    // append div buttons to td
                    taskButtonsActionsTd.appendChild(divButtonsElement);

                    // append checkbox td to tr
                    tableRaw.appendChild(tdCheckboxEle);

                    // append title td to tr
                    tableRaw.appendChild(tdTaskTitleTd);

                    // append status td to tr
                    tableRaw.appendChild(tdTaskTypeTd);

                    // append created at td to tr
                    tableRaw.appendChild(taskCreatedAtTd);

                    // append due date td to tr
                    tableRaw.appendChild(taskDueDateTd);

                    // append buttons td to tr
                    tableRaw.appendChild(taskButtonsActionsTd);

                    // append the row to tbody
                    tableBody.appendChild(tableRaw);
                  });
                  // view task buttons
                  const bookkeeperTaskViewBtns = document.querySelectorAll(
                    "button.bookkeeperTaskViewBtn",
                  );
                  bookkeeperTaskViewBtns.forEach((btn) => {
                    btn.addEventListener("click", (event) => {
                      const currentTarget = event.currentTarget;
                      const retrieveTaskUrl = window.localStorage.getItem("retrieveTaskUrl");
                      const taskId = currentTarget.dataset["taskId"];
                      // console.log(taskId);
                      const requestOptions = {
                        method: "POST",
                        dataToSend: { taskId: taskId },
                        url: retrieveTaskUrl,
                      };
                      const request = sendRequest(requestOptions);
                      request
                        .then((taskData) => {
                          const taskDetails = taskData["task"];
                          const jobDetails = taskDetails["job"];
                          const taskDetailsModalForm = document.querySelector(
                            "form#taskDetailsModalForm",
                          );
                          const taskDetailsModalCallbacks = {
                            onOpenCallBack: () => {
                              taskDetailsModalForm["job_title"].value = jobDetails["title"];
                              taskDetailsModalForm["title"].value = taskDetails["title"];
                              taskDetailsModalForm["task_type"].value = taskDetails["task_type"];
                              taskDetailsModalForm["hints"].value = taskDetails["hints"];
                              if (taskDetails["is_completed"] === true) {
                                taskDetailsModalForm["is_completed"].checked = true;
                              } else {
                                taskDetailsModalForm["is_completed"].checked = false;
                              }
                              taskDetailsModalForm["additional_notes"].value =
                                taskDetails["additional_notes"];
                              taskDetailsModalForm["start_date"].value = taskDetails["start_date"];
                              taskDetailsModalForm["due_date"].value = taskDetails["due_date"];
                            },
                            onCloseCallback: () => {
                              console.warn("close details task item");
                            },
                          };
                          new MicroModalHandler("task-details-modal", taskDetailsModalCallbacks);

                          // console.log(tasks);
                          // showToastNotification(data["msg"], "success");
                          /* setTimeout(() => {
                            window.location.reload();
                          }, 500); */
                        })
                        .catch((error) => {
                          console.error(error);
                          showToastNotification(
                            `${JSON.stringify(error["user_error_msg"])}`,
                            "danger",
                          );
                        })
                        .finally(() => {
                          // jobsFormFieldset.disabled = false;
                          // managerJobsLoaderBtn.hidden = true;
                        });
                    });
                  });
                }
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
              });
          },
          onCloseCallback: () => {
            console.log("on close");
            noTasksNotification.hidden = true;
            jobTasksTable.querySelector("tbody").innerHTML = "";
            tasksItemsModalTitle.textContent = "";
          },
        };
        const modlaHandler = new MicroModalHandler("tasks-items-modal", callBacks);
      });
    });

    // update task button event
    updateTaskBookkeeperBtn.addEventListener("click", (event) => {
      event.preventDefault();
      const checkedTasksArray = new Array();
      const tasksInputs = document.querySelectorAll(".tasks-checkbox");
      tasksInputs.forEach((input) => {
        const taskId = input.dataset["taskId"];
        const isCompleted = Boolean(input.dataset["isCompleted"]);

        if (input.checked === true && isCompleted === false) {
          checkedTasksArray.push(taskId);
        }
      });

      if (checkedTasksArray.length > 0) {
        const setTaskCompletedUrl = window.localStorage.getItem("setTaskCompletedUrl");
        const requestOptions = {
          method: "PUT",
          dataToSend: { tasks: checkedTasksArray },
          url: setTaskCompletedUrl,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            const tasks = data["tasks"];
            tasks.forEach((element) => {
              const trElement = document.querySelector(`tr[data-task-id="${element}"]`);
              trElement.classList.add(...["has-background-grey-lighter"]);
              trElement.childNodes.forEach((node) => {
                const tdName = node.dataset["tdName"];
                switch (tdName) {
                  case "task-td-checkbox":
                    const input = node.querySelector("input[type='checkbox']");
                    input.setAttribute("data-is-completed", "1");
                    input.checked = true;
                    input.disabled = true;
                    break;
                  case "task-td-title":
                    node.classList.add(...["completed-task-item"]);
                    break;

                  default:
                    break;
                }
                // console.log(node);
                // console.log(node.dataset);
              });
            });
            // console.log(tasks);
            showToastNotification(data["msg"], "success");
            /* setTimeout(() => {
              window.location.reload();
            }, 500); */
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            // jobsFormFieldset.disabled = false;
            // managerJobsLoaderBtn.hidden = true;
          });
      }
    });

    // delete task buttons
    const deleteTaskBtns = document.querySelectorAll(".delete-task-btn");
    deleteTaskBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        alert("do you want to delete?");
      });
    });

    // tasks checkbox main checkbox event
    const tasksThMainCheckboxs = document.querySelectorAll(".tasks-th-main-checkbox");

    tasksThMainCheckboxs.forEach((element) => {
      element.addEventListener("change", (event) => {
        const currentTarget = event.currentTarget;

        const childeElementsCssClass = `.${currentTarget.dataset["childCheckboxClass"]}`;
        const allChildElements = document.querySelectorAll(childeElementsCssClass);
        allChildElements.forEach((input) => {
          // console.log(weeklyTasksInputs);
          const setDisabled = Boolean(input.dataset["setDisabled"]);
          if (setDisabled === false) {
            if (currentTarget.checked === true) {
              input.checked = true;
            } else {
              input.checked = false;
            }
          }
        });
      });
    });

    document.querySelectorAll(".tablinks").forEach((element) => {
      element.addEventListener("click", (event) => {
        let i, tabcontent, tablinks;
        const clickedBtn = event.currentTarget;
        const data = clickedBtn.dataset;
        const tabContentId = data["tabElement"];
        tabcontent = document.querySelectorAll(".tabcontent");
        tabcontent.forEach((tabElement) => {
          tabElement.style.display = "none";
        });
        tablinks = document.querySelectorAll(".tablinks");
        tablinks.forEach((linkElement) => {
          linkElement.className = linkElement.className.replace("active", "");
        });
        document.querySelector(`#${tabContentId}`).style.display = "block";
        clickedBtn.classList.add("active");
      });
    });

    document.querySelectorAll(".tablinks2").forEach((element) => {
      element.addEventListener("click", (event) => {
        let i, tabcontent, tablinks;
        const clickedBtn = event.currentTarget;
        const data = clickedBtn.dataset;
        const tabContentId = data["tabElement"];
        tabcontent = document.querySelectorAll(".tabcontent2");
        tabcontent.forEach((tabElement) => {
          tabElement.style.display = "none";
        });
        tablinks = document.querySelectorAll(".tablinks2");
        tablinks.forEach((linkElement) => {
          linkElement.className = linkElement.className.replace("active", "");
        });
        document.querySelector(`#${tabContentId}`).style.display = "block";
        clickedBtn.classList.add("active");
      });
    });

    // Get the element with id="defaultOpen" and click on it
    // document.getElementById("defaultOpen").click();
    document.querySelectorAll(".defaultOpenTab1").forEach((element) => {
      element.click();
    });

    const acc = document.querySelectorAll(".accordion");
    let i;
    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }

    const copyASurlBtns = document.querySelectorAll(".copyASurlBtn");
    copyASurlBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const UrlInputId = currentTarget.dataset["clipboardTarget"];
        const UrlInputElement = document.querySelector(`${UrlInputId}`);
      });
    });

    const allShowASPasswordBtns = document.querySelectorAll(".showASUPasswordBtn");
    allShowASPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const visibilityStatus = Boolean(parseInt(currentTarget.dataset["visibilityStatus"]));
        const passwordInputId = currentTarget.dataset["passwordInput"];
        const passwordInputElement = document.querySelector(`#${passwordInputId}`);
        if (visibilityStatus === true) {
          currentTarget.innerHTML = eyeIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 0;
          passwordInputElement.type = "password";
        } else {
          currentTarget.innerHTML = eyeSlashIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 1;
          passwordInputElement.type = "text";
        }
      });
    });

    clipboardJs.on("success", (e) => {
      // console.info("Action:", e.action);
      // console.info("Text:", e.text);
      // console.info("Trigger:", e.trigger);
      e.clearSelection();
      const copiedText = e.text;
      const element = e.trigger;
      const textType = element.dataset["textType"];
      switch (textType) {
        case "username":
          showToastNotification(`Username ${copiedText} copied successfully`, "success");
          break;

        case "password":
          showToastNotification(`Password copied successfully`, "success");
          break;
        case "url":
          showToastNotification(`Url copied successfully`, "success");
          break;
      }
    });

    // open note item
    const allNotesItemsBtns = document.querySelectorAll(".open-note-item-btn");
    allNotesItemsBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        MicroModal.show("notes-item-modal", {
          disableScroll: false,
          onClose: (modal) => {
            console.info(`${modal.id} is hidden`);
          },
          disableFocus: false,
        });
      });
    });

    const tableFooterSearchElements = document.querySelectorAll(
      "#clientsAccountAndServicesTable tfoot th",
    );
    tableFooterSearchElements.forEach((element) => {
      const title = element.textContent;
      let inputID;
      switch (element.id) {
        case "footerUrl":
          inputID = "searchFooterUrl";
          break;
        case "footerUsername":
          inputID = "searchFooterUsername";
          break;
        case "footerPassword":
          inputID = "searchFooterPassword";
          break;
      }
      // element.innerHTML = '<input type="text" placeholder="Search ' + title + '" />';
      const searchInputElement = document.createElement("input");
      searchInputElement.type = "text";
      searchInputElement.id = inputID;
      searchInputElement.classList.add(...["input", "is-small", "searchTableFooterInput"]);
      searchInputElement.placeholder = `Search ${title}`;
      element.appendChild(searchInputElement);
    });

    const clientsAccountAndServicesTable = $("#clientsAccountAndServicesTable").DataTable({
      autoWidth: true,
      // processing: true,
      info: true,
      // "paging": false,
      // stateSave: true,
      stateSaveCallback: function (settings, data) {
        localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
      },
      stateLoadCallback: function (settings) {
        return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
      },
      fixedHeader: true,
      // responsive: true,
      columnDefs: [{ type: "html-input", targets: [0, 1, 2] }],
      // dom: "Bfrtip",
      /* buttons: [
        {
          extend: "alert",
          text: "My button 1",
        },
        {
          extend: "alert",
          text: "My button 2",
        },
        {
          extend: "alert",
          text: "My button 3",
        },
      ], */
      // buttons: ["copy", "csv", "pdf"],
      initComplete: function () {
        // Apply the search
        this.api()
          .columns()
          .every(function () {
            let that = this;
            // console.log(this.footer());
            $("input", this.footer()).on("keyup change clear", function () {
              if (that.search() !== this.value) {
                that.search(this.value).draw();
              }
            });
          });
      },
    });
    // Apply the search
    clientsAccountAndServicesTable.columns().every(function () {
      let that = this;

      $("input", this.footer()).on("keyup change", function () {
        that.search(this.value).draw();
      });
    });
  }
});
