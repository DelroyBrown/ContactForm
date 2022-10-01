$(document).ready(function () {
  $("#id_logo_1").change(function () {
    if ($("#id_logo_1").val() == "no") {
      console.log("you hit no");
      $("#logoCreated").addClass("appear");
    }
  });
  $("#id_logo_0").change(function () {
    if ($("#id_logo_0").val() == "yes") {
      console.log("you hit yes");
      $("#logoCreated").removeClass("appear");
    }
  });




});
