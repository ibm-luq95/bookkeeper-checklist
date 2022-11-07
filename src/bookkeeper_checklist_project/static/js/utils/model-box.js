"use strict";

const showMicroModal = (modalId, onCloseCallback) => {
  MicroModal.show(modalId, {
    disableScroll: false,
    onClose: (modal) => {
      //   console.info(`${modal.id} is hidden`);
      if (typeof onCloseCallback == "function") {
        onCloseCallback();
      }
    },
    disableFocus: false,
  });
};

export { showMicroModal };
