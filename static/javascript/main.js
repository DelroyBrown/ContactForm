$(document).ready(function () {
  $("#id_logo").change(function () {
    if ($("#id_logo_1").val() == "no") {
      console.log("you hit no");
      $("#logoCreated").addClass("appear");
    }
  });
  $("#id_products_product_images").change(function () {
    if ($("#id_products_product_images_1").val() == "no") {
      console.log("you hit no");
      $("#photographer").addClass("appear");
    }
  });
});
