(function ($) {
  "use strict";
  Drupal.behaviors.trialClientValidation = {
    attach: function (context) {
      console.log('JS loaded in Trial module.');
      $(document).bind('clientsideValidationAddCustomRules', function(event){
        jQuery.validator.addMethod("taboo", function(value, element, param) {
//          console.log('value', value);
//          console.log('element', element);
//          console.log('param', param);

          return value !== param;
        });
      });

//      Drupal.clientsideValidation.prototype.mycustomerrorplacement = function (error, element) {
//      };
    }
  };
})(jQuery);