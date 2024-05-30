/******/ // The require scope
/******/ var __webpack_require__ = {};
/******/
/************************************************************************/
/******/ /* webpack/runtime/define property getters */
/******/ (() => {
    /******/ 	// define getter functions for harmony exports
    /******/ 	__webpack_require__.d = (exports, definition) => {
        /******/ 		for(var key in definition) {
            /******/ 			if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
                /******/ 				Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
                /******/ 			}
            /******/ 		}
        /******/ 	};
    /******/ })();
/******/
/******/ /* webpack/runtime/hasOwnProperty shorthand */
/******/ (() => {
    /******/ 	__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
    /******/ })();
/******/
/******/ /* webpack/runtime/make namespace object */
/******/ (() => {
    /******/ 	// define __esModule on exports
    /******/ 	__webpack_require__.r = (exports) => {
        /******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
            /******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
            /******/ 		}
        /******/ 		Object.defineProperty(exports, '__esModule', { value: true });
        /******/ 	};
    /******/ })();
/******/
/************************************************************************/
var __webpack_exports__ = {};
/*!*************************************!*\
  !*** ./reactsrc/CustomInputCell.js ***!
  \*************************************/
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
    /* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
    /* harmony export */ });
function _classCallCheck(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function");
    }
}

function _defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
        var descriptor = props[i];
        descriptor.enumerable = descriptor.enumerable || false;
        descriptor.configurable = true;
        if ("value" in descriptor) descriptor.writable = true;
        Object.defineProperty(target, descriptor.key, descriptor);
    }
}

function _createClass(Constructor, protoProps, staticProps) {
    if (protoProps) _defineProperties(Constructor.prototype, protoProps);
    if (staticProps) _defineProperties(Constructor, staticProps);
    Object.defineProperty(Constructor, "prototype", {
        writable: false
    });
    return Constructor;
}

var CustomInputCell = /*#__PURE__*/function () {
    /**
     * Custom Row Cell
     * @constructor
     * @param {object} globalConfig - Global configuration.
     * @param {string} serviceName - Input service name.
     * @param {element} el - The element of the custom cell.
     * @param {object} row - The object containing current values of row.
     * @param {string} field - Custom cell field name.
     */
    function CustomInputCell(globalConfig, serviceName, el, row, field) {
        _classCallCheck(this, CustomInputCell);

        this.globalConfig = globalConfig;
        this.serviceName = serviceName;
        this.el = el;
        this.row = row;
        this.field = field;
    }

    _createClass(CustomInputCell, [{
        key: "render",
        value: function render(row, field) {
            var _this = this;

            var html = "";
            var entity = this.globalConfig.pages.inputs.services.find(function (x) {
                return x.name === _this.serviceName;
            });

            if (field == "input") {
                html = entity.title;
            } else {
                html = "Unknown";
            }

            this.el.innerHTML = html;
            return this;
        }
    }]);

    return CustomInputCell;
}();

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (CustomInputCell);
var __webpack_exports__default = __webpack_exports__["default"];
export { __webpack_exports__default as default };

//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiQ3VzdG9tSW5wdXRDZWxsLmpzIiwibWFwcGluZ3MiOiJTQUFBO1NBQ0E7Ozs7O1VDREE7VUFDQTtVQUNBO1VBQ0E7VUFDQSx5Q0FBeUMsd0NBQXdDO1VBQ2pGO1VBQ0E7VUFDQTs7Ozs7VUNQQTs7Ozs7VUNBQTtVQUNBO1VBQ0E7VUFDQSx1REFBdUQsaUJBQWlCO1VBQ3hFO1VBQ0EsZ0RBQWdELGFBQWE7VUFDN0Q7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7SUNOTUE7RUFDRjtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7RUFDSSx5QkFBWUMsWUFBWixFQUEwQkMsV0FBMUIsRUFBdUNDLEVBQXZDLEVBQTJDQyxHQUEzQyxFQUFnREMsS0FBaEQsRUFBdUQ7SUFBQUM7O0lBQ25ELEtBQUtMLFlBQUwsR0FBb0JBLFlBQXBCO0lBQ0EsS0FBS0MsV0FBTCxHQUFtQkEsV0FBbkI7SUFDQSxLQUFLQyxFQUFMLEdBQVVBLEVBQVY7SUFDQSxLQUFLQyxHQUFMLEdBQVdBLEdBQVg7SUFDQSxLQUFLQyxLQUFMLEdBQWFBLEtBQWI7RUFDSDs7OztXQUVELGdCQUFPRCxHQUFQLEVBQVlDLEtBQVosRUFBbUI7TUFBQTs7TUFDZixJQUFJRSxJQUFJLEdBQUcsRUFBWDtNQUNBLElBQUlDLE1BQU0sR0FBRyxLQUFLUCxZQUFMLENBQWtCUSxLQUFsQixDQUF3QkMsTUFBeEIsQ0FBK0JDLFFBQS9CLENBQXdDQyxJQUF4QyxDQUNULFVBQUNDLENBQUQ7UUFBQSxPQUFPQSxDQUFDLENBQUNDLElBQUZELEtBQVdFLEtBQUksQ0FBQ2IsV0FBdkI7TUFEUyxFQUFiOztNQUdBLElBQUlHLEtBQUssSUFBSSxPQUFiLEVBQXNCO1FBQ2xCRSxJQUFJLEdBQUdDLE1BQU0sQ0FBQ1EsS0FBZFQ7TUFESixPQUVPO1FBQ0hBLElBQUksR0FBRyxTQUFQQTtNQUNIOztNQUNELEtBQUtKLEVBQUwsQ0FBUWMsU0FBUixHQUFvQlYsSUFBcEI7TUFDQSxPQUFPLElBQVA7SUFDSDs7Ozs7O0FBR0wsaUVBQWVQLGVBQWYsRSIsInNvdXJjZXMiOlsid2VicGFjazovL1RBLW9jdG9wdXNlbmVyZ3kvd2VicGFjay9ib290c3RyYXAiLCJ3ZWJwYWNrOi8vVEEtb2N0b3B1c2VuZXJneS93ZWJwYWNrL3J1bnRpbWUvZGVmaW5lIHByb3BlcnR5IGdldHRlcnMiLCJ3ZWJwYWNrOi8vVEEtb2N0b3B1c2VuZXJneS93ZWJwYWNrL3J1bnRpbWUvaGFzT3duUHJvcGVydHkgc2hvcnRoYW5kIiwid2VicGFjazovL1RBLW9jdG9wdXNlbmVyZ3kvd2VicGFjay9ydW50aW1lL21ha2UgbmFtZXNwYWNlIG9iamVjdCIsIndlYnBhY2s6Ly9UQS1vY3RvcHVzZW5lcmd5Ly4vcmVhY3RzcmMvQ3VzdG9tSW5wdXRDZWxsLmpzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIFRoZSByZXF1aXJlIHNjb3BlXG52YXIgX193ZWJwYWNrX3JlcXVpcmVfXyA9IHt9O1xuXG4iLCIvLyBkZWZpbmUgZ2V0dGVyIGZ1bmN0aW9ucyBmb3IgaGFybW9ueSBleHBvcnRzXG5fX3dlYnBhY2tfcmVxdWlyZV9fLmQgPSAoZXhwb3J0cywgZGVmaW5pdGlvbikgPT4ge1xuXHRmb3IodmFyIGtleSBpbiBkZWZpbml0aW9uKSB7XG5cdFx0aWYoX193ZWJwYWNrX3JlcXVpcmVfXy5vKGRlZmluaXRpb24sIGtleSkgJiYgIV9fd2VicGFja19yZXF1aXJlX18ubyhleHBvcnRzLCBrZXkpKSB7XG5cdFx0XHRPYmplY3QuZGVmaW5lUHJvcGVydHkoZXhwb3J0cywga2V5LCB7IGVudW1lcmFibGU6IHRydWUsIGdldDogZGVmaW5pdGlvbltrZXldIH0pO1xuXHRcdH1cblx0fVxufTsiLCJfX3dlYnBhY2tfcmVxdWlyZV9fLm8gPSAob2JqLCBwcm9wKSA9PiAoT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iaiwgcHJvcCkpIiwiLy8gZGVmaW5lIF9fZXNNb2R1bGUgb24gZXhwb3J0c1xuX193ZWJwYWNrX3JlcXVpcmVfXy5yID0gKGV4cG9ydHMpID0+IHtcblx0aWYodHlwZW9mIFN5bWJvbCAhPT0gJ3VuZGVmaW5lZCcgJiYgU3ltYm9sLnRvU3RyaW5nVGFnKSB7XG5cdFx0T2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsIFN5bWJvbC50b1N0cmluZ1RhZywgeyB2YWx1ZTogJ01vZHVsZScgfSk7XG5cdH1cblx0T2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsICdfX2VzTW9kdWxlJywgeyB2YWx1ZTogdHJ1ZSB9KTtcbn07IiwiY2xhc3MgQ3VzdG9tSW5wdXRDZWxsIHtcbiAgICAvKipcbiAgICAgKiBDdXN0b20gUm93IENlbGxcbiAgICAgKiBAY29uc3RydWN0b3JcbiAgICAgKiBAcGFyYW0ge29iamVjdH0gZ2xvYmFsQ29uZmlnIC0gR2xvYmFsIGNvbmZpZ3VyYXRpb24uXG4gICAgICogQHBhcmFtIHtzdHJpbmd9IHNlcnZpY2VOYW1lIC0gSW5wdXQgc2VydmljZSBuYW1lLlxuICAgICAqIEBwYXJhbSB7ZWxlbWVudH0gZWwgLSBUaGUgZWxlbWVudCBvZiB0aGUgY3VzdG9tIGNlbGwuXG4gICAgICogQHBhcmFtIHtvYmplY3R9IHJvdyAtIFRoZSBvYmplY3QgY29udGFpbmluZyBjdXJyZW50IHZhbHVlcyBvZiByb3cuXG4gICAgICogQHBhcmFtIHtzdHJpbmd9IGZpZWxkIC0gQ3VzdG9tIGNlbGwgZmllbGQgbmFtZS5cbiAgICAgKi9cbiAgICBjb25zdHJ1Y3RvcihnbG9iYWxDb25maWcsIHNlcnZpY2VOYW1lLCBlbCwgcm93LCBmaWVsZCkge1xuICAgICAgICB0aGlzLmdsb2JhbENvbmZpZyA9IGdsb2JhbENvbmZpZztcbiAgICAgICAgdGhpcy5zZXJ2aWNlTmFtZSA9IHNlcnZpY2VOYW1lO1xuICAgICAgICB0aGlzLmVsID0gZWw7XG4gICAgICAgIHRoaXMucm93ID0gcm93O1xuICAgICAgICB0aGlzLmZpZWxkID0gZmllbGQ7XG4gICAgfVxuXG4gICAgcmVuZGVyKHJvdywgZmllbGQpIHtcbiAgICAgICAgbGV0IGh0bWwgPSBcIlwiO1xuICAgICAgICBsZXQgZW50aXR5ID0gdGhpcy5nbG9iYWxDb25maWcucGFnZXMuaW5wdXRzLnNlcnZpY2VzLmZpbmQoXG4gICAgICAgICAgICAoeCkgPT4geC5uYW1lID09PSB0aGlzLnNlcnZpY2VOYW1lXG4gICAgICAgICk7XG4gICAgICAgIGlmIChmaWVsZCA9PSBcImlucHV0XCIpIHtcbiAgICAgICAgICAgIGh0bWwgPSBlbnRpdHkudGl0bGVcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIGh0bWwgPSBcIlVua25vd25cIlxuICAgICAgICB9XG4gICAgICAgIHRoaXMuZWwuaW5uZXJIVE1MID0gaHRtbDtcbiAgICAgICAgcmV0dXJuIHRoaXM7XG4gICAgfVxufVxuXG5leHBvcnQgZGVmYXVsdCBDdXN0b21JbnB1dENlbGw7Il0sIm5hbWVzIjpbIkN1c3RvbUlucHV0Q2VsbCIsImdsb2JhbENvbmZpZyIsInNlcnZpY2VOYW1lIiwiZWwiLCJyb3ciLCJmaWVsZCIsIl9jbGFzc0NhbGxDaGVjayIsImh0bWwiLCJlbnRpdHkiLCJwYWdlcyIsImlucHV0cyIsInNlcnZpY2VzIiwiZmluZCIsIngiLCJuYW1lIiwiX3RoaXMiLCJ0aXRsZSIsImlubmVySFRNTCJdLCJzb3VyY2VSb290IjoiIn0=