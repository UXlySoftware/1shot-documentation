OpenAPI Specification
----------------------

.. raw:: html

   <div id="swagger-ui"></div>
   <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css">
   <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
   <script>
     window.onload = () => {
       SwaggerUIBundle({
         url: "../_static/m2mGatewaySpec.yaml",
         dom_id: "#swagger-ui",
         presets: [
           SwaggerUIBundle.presets.apis,
           SwaggerUIBundle.SwaggerUIStandalonePreset
         ],
         layout: "BaseLayout"
       });
     };
   </script>