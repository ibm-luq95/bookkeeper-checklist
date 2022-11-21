"use strict";

const showMicroModal = (modalId, onCloseCallback, onOpenCallBack) => {
  MicroModal.show(modalId, {
    disableScroll: false,
    onClose: (modal) => {
      //   console.info(`${modal.id} is hidden`);
      if (typeof onCloseCallback == "function") {
        onCloseCallback();
      }
    },
    onShow: (modal) => {
      //   console.info(`${modal.id} is hidden`);
      if (typeof onOpenCallBack == "function") {
        onOpenCallBack();
      }
    },

    disableFocus: false,
  });
};

class MicroModalHandler {
  constructor(modalId, callBacks) {
    this.modalId = modalId;
    if (typeof callBacks["onCloseCallback"] == "function") {
      this.onCloseCallback = callBacks["onCloseCallback"];
    }
    if (typeof callBacks["onOpenCallBack"] == "function") {
      this.onOpenCallBack = callBacks["onOpenCallBack"];
    }

    this.fireModal();
  }

  fireModal() {
    MicroModal.show(this.modalId, {
      disableScroll: false,
      onClose: (modal) => {
        //   console.info(`${modal.id} is hidden`);
        if (typeof this.onCloseCallback == "function") {
          this.onCloseCallback();
        }
      },
      onShow: (modal) => {
        //   console.info(`${modal.id} is hidden`);
        if (typeof this.onOpenCallBack == "function") {
          this.onOpenCallBack();
        }
      },

      disableFocus: false,
    });
  }
}

export { showMicroModal, MicroModalHandler };
