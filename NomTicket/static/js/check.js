function compra(){
    var escogidos = $('input[name=webcampics[]]:checked');
    for2 = "";
      escogidos.each(function(){
        for2 = for2 + $this.val() + "-";
      },
      VentanaCentrada('./pdf/documentos/ordendecompra_pdf.php?for2='+for2+'Cotizacion','','1024','768','true')
}