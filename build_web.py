#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Genera un index.html autocontenido (HTML+CSS+JS+curso) que funciona con file://"""
import json, os

course = json.load(open('data/course.json', encoding='utf-8'))
data = json.dumps(course, ensure_ascii=False)

HTML = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Python Learn - Curso Interactivo Gratuito</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0d1117;--panel:#161b22;--panel2:#1c2431;--line:#2b3646;--txt:#e6edf3;--dim:#8b98a9;--cyan:#22d3ee;--green:#3fb950;--yel:#d29922;--pur:#a371f7;--red:#f85149}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--txt)}
button{font-family:inherit;cursor:pointer}
#layout{display:flex;min-height:100vh}
aside{width:290px;flex-shrink:0;background:var(--panel);border-right:1px solid var(--line);display:flex;flex-direction:column;position:sticky;top:0;height:100vh}
.brand{padding:20px;border-bottom:1px solid var(--line);text-align:center}
.brand .logo{font-size:40px}
.brand h1{font-size:20px;color:var(--cyan);margin-top:4px}
.brand small{color:var(--dim);font-size:12px}
.hud{display:grid;grid-template-columns:repeat(3,1fr);padding:14px;background:var(--panel2);border-bottom:1px solid var(--line);text-align:center}
.hud b{display:block;font-size:18px;color:var(--cyan)}
.hud span{font-size:11px;color:var(--dim)}
#secList{flex:1;overflow-y:auto;padding:8px}
.sec{border-bottom:1px solid var(--line);padding:8px 10px}
.sec h3{font-size:12px;color:var(--dim);text-transform:uppercase;letter-spacing:.5px;margin:6px 0}
.sec a{display:flex;gap:8px;align-items:center;padding:7px 9px;border-radius:6px;color:var(--txt);text-decoration:none;font-size:13px}
.sec a:hover{background:var(--panel2)}
.sec a.on{background:#1f6feb33;border-left:3px solid var(--cyan)}
.dot{width:9px;height:9px;border-radius:50%;background:#30363d;flex-shrink:0}
.dot.done{background:var(--green)}
.dot.proj{background:var(--yel)}
main{flex:1;min-width:0;display:flex;flex-direction:column}
#top{display:flex;align-items:center;gap:12px;padding:12px 20px;border-bottom:1px solid var(--line);background:var(--panel);position:sticky;top:0;z-index:5}
#top h2{font-size:18px;flex:1}
.ghost{background:transparent;border:1px solid var(--line);color:var(--dim);padding:7px 13px;border-radius:7px;font-size:13px}
.ghost:hover{border-color:var(--cyan);color:var(--cyan)}
.bar{height:5px;background:var(--panel2)}
.bar div{height:100%;background:linear-gradient(90deg,var(--cyan),var(--green));transition:width .4s}
#body{flex:1;padding:22px;max-width:920px;width:100%;margin:0 auto}
.hero{text-align:center;padding:70px 20px}
.hero h2{font-size:38px;color:var(--cyan)}
.hero p{color:var(--dim);margin:10px 0}
.btn{background:linear-gradient(135deg,#22d3ee,#0ea5e9);border:0;color:#04222a;font-weight:700;padding:13px 34px;border-radius:10px;font-size:16px}
.btn:hover{filter:brightness(1.1)}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:20px;margin-bottom:16px}
.card h3{color:#fff;font-size:19px;margin-bottom:6px}
.card .desc{color:var(--dim);font-size:14px}
.badge{display:inline-block;padding:2px 9px;border-radius:20px;font-size:11px;font-weight:600}
.b-learn{background:#1f4b7355;color:#58a6ff}
.b-prac{background:#2d6a3555;color:var(--green)}
.b-proj{background:#6b4a1455;color:var(--yel)}
pre{background:#010409;border:1px solid var(--line);border-radius:9px;padding:14px;overflow-x:auto;font-family:Consolas,Monaco,monospace;font-size:13px;color:#7ee787;line-height:1.6}
.ex{background:var(--panel2);border-left:3px solid var(--cyan);border-radius:0 9px 9px 0;padding:14px;margin:12px 0}
.ex .q{font-weight:600;margin-bottom:8px}
.ex .h{color:var(--dim);font-size:13px;margin-top:8px}
.ex .h b{color:var(--yel)}
textarea{width:100%;background:#010409;color:#7ee787;border:1px solid var(--line);border-radius:8px;padding:11px;font-family:Consolas,Monaco,monospace;font-size:13px;min-height:70px;resize:vertical}
textarea:focus{outline:none;border-color:var(--cyan)}
.row{display:flex;gap:8px;margin-top:9px;flex-wrap:wrap}
.ok{color:var(--green);font-weight:600;margin-top:8px}
.no{color:var(--red);font-weight:600;margin-top:8px}
.nav{display:flex;gap:9px;margin-top:18px;flex-wrap:wrap}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:11px}
.tcard{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:15px;text-align:center}
.tcard:hover{border-color:var(--cyan)}
.tcard.ok{border-color:var(--green)}
.tcard .n{font-size:19px;font-weight:700;color:var(--cyan)}
.tcard.ok .n{color:var(--green)}
.tcard .t{font-size:12px;color:var(--dim);margin-top:5px}
.gridlessons{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:11px}
.lcard{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:15px;text-align:center}
.lcard:hover{border-color:var(--cyan)}
.lcard .n{font-size:22px;font-weight:700;color:var(--cyan)}
.lcard .t{font-size:12px;color:var(--dim);margin:5px 0}
.cert{text-align:center;padding:44px;background:linear-gradient(135deg,#161b22,#1f2937);border:2px solid var(--yel);border-radius:14px}
.cert h2{color:var(--yel);font-size:28px}
.cert p{color:var(--dim);margin:9px 0}
@media(max-width:800px){#layout{flex-direction:column}aside{width:100%;height:auto;position:relative}#secList{max-height:210px}#body{padding:15px}.hero h2{font-size:27px}}
</style>
</head>
<body>
<div id="layout">
<aside>
  <div class="brand">
    <div class="logo">&#128045;</div>
    <h1>Python Learn</h1>
    <small>Curso interactivo gratuito</small>
  </div>
  <div class="hud">
    <div><b id="hScore">0</b><span>&#11088; Puntos</span></div>
    <div><b id="hDone">0</b><span>&#128218; Temas</span></div>
    <div><b id="hStreak">0</b><span>&#128293; Racha</span></div>
  </div>
  <div id="secList"></div>
</aside>
<main>
  <div id="top">
    <button class="ghost" onclick="goHome()">&#127968; Inicio</button>
    <h2 id="ttl">Python Learn</h2>
    <button class="ghost" onclick="showCert()">&#127942; Certificado</button>
  </div>
  <div class="bar"><div id="pfill" style="width:0%"></div></div>
  <div id="body"></div>
</main>
</div>
<script>
var COURSE = __DATA__;
var SECS = __SECS__;
var S = {done:[],score:0,streak:0};

function loadS(){try{var s=localStorage.getItem('pl_v1');if(s)S=JSON.parse(s);}catch(e){}}
function saveS(){try{localStorage.setItem('pl_v1',JSON.stringify(S));}catch(e){}}
function topicsOf(l){return (l.topics&&l.topics.length)?l.topics:[{title:l.title,description:'',exercises:l.exercises||[]}];}
function allItems(){var o=[];Object.keys(COURSE).sort(function(a,b){return a-b;}).forEach(function(id){topicsOf(COURSE[id]).forEach(function(t,i){o.push({lid:id,tid:i,lesson:COURSE[id],topic:t});});});return o;}
function key(lid,tid){return lid+'_'+tid;}
function badge(l){if(l.type==='PROJECT_GUIDED')return '<span class="badge b-proj">Proyecto guiado</span>';if(l.type==='PRACTICE')return '<span class="badge b-prac">Practica</span>';return '<span class="badge b-learn">Aprende</span>';}
function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function hud(){document.getElementById('hScore').textContent=S.score;document.getElementById('hStreak').textContent=S.streak;document.getElementById('hDone').textContent=S.done.length+'/'+allItems().length;document.getElementById('pfill').style.width=(S.done.length/allItems().length*100)+'%';}

function nav(){
  var h='';
  SECS.forEach(function(sec){
    var n=0;sec.ls.forEach(function(id){n+=topicsOf(COURSE[id]).length;});
    var dn=0;sec.ls.forEach(function(id){topicsOf(COURSE[id]).forEach(function(t,i){if(S.done.indexOf(key(id,i))>-1)dn++;});});
    h+='<div class="sec"><h3>'+(dn===n?'&#10004; ':'')+esc(sec.n)+' ('+dn+'/'+n+')</h3>';
    sec.ls.forEach(function(id){
      var l=COURSE[id],t=topicsOf(l);
      var d=t.every(function(x,i){return S.done.indexOf(key(id,i))>-1;});
      h+='<a href="#" data-g="l" data-id="'+id+'"><span class="dot'+(d?' done':'')+(l.type==='PROJECT_GUIDED'?' proj':'')+'"></span><span>'+id+'. '+esc(l.title)+'</span></a>';
    });
    h+='</div>';
  });
  document.getElementById('secList').innerHTML=h;
  Array.prototype.forEach.call(document.querySelectorAll('#secList a'),function(a){
    a.onclick=function(e){e.preventDefault();showLesson(a.dataset.id);};
  });
}

function goHome(){
  document.getElementById('ttl').textContent='Python Learn';
  var n=allItems().length,p=S.done.length,r=Math.round(p/n*100);
  document.getElementById('body').innerHTML =
   '<div class="hero"><div class="logo" style="font-size:64px">&#128045;</div>'+
   '<h2>Python Learn</h2><p>Curso interactivo de Python, gratis y en tu navegador</p>'+
   '<p style="color:#22d3ee;font-weight:600">'+n+' temas &middot; 14 proyectos &middot; 100% gratis</p>'+
   '<br><button class="btn" onclick="nextTopic()">&#9654; Empezar a aprender</button>'+
   (p? '<p style="margin-top:18px;font-size:14px">Progreso: '+p+'/'+n+' ('+r+'%)</p>':'')+
   '<p style="margin-top:26px;font-size:12px;color:#6e7b8c">Inspirado en Mimo &middot; offline, sin servidor</p></div>';
  nav();hud();
}

function nextTopic(){
  var it=allItems(),n=S.done.length;
  for(var i=0;i<it.length;i++){if(S.done.indexOf(key(it[i].lid,it[i].tid))===-1){showTopic(it[i].lid,it[i].tid);return;}}
  showCert();
}

function showLesson(id){
  var l=COURSE[id],t=topicsOf(l);
  document.getElementById('ttl').textContent=l.title;
  var h='<div class="card"><h3>'+id+'. '+esc(l.title)+'</h3><div class="desc">'+badge(l)+'</div>'+
        (l.project_code?'<p style="color:#8b98a9;font-size:14px;margin-top:10px">'+esc(l.project_code.split('\\n')[0])+'</p>':'')+'</div><div class="grid">';
  t.forEach(function(x,i){
    var d=S.done.indexOf(key(id,i))>-1;
    h+='<div class="tcard'+(d?' ok':'')+'" onclick="showTopic('+id+','+i+')"><div class="n">'+(d?'&#10004;':(i+1))+'</div><div class="t">'+esc(x.title)+'</div></div>';
  });
  h+='</div><div class="nav"><button class="btn" onclick="nextTopic()">Continuar &#9654;</button><button class="ghost" onclick="goHome()">Inicio</button></div>';
  document.getElementById('body').innerHTML=h;nav();hud();
}

function showTopic(lid,tid){
  var l=COURSE[lid],t=topicsOf(l)[tid];
  document.getElementById('ttl').textContent=t.title;
  var h='<div class="card"><h3>'+esc(t.title)+'</h3><div class="desc">'+badge(l)+' &middot; Leccion '+lid+', tema '+(tid+1)+'</div>'+
        (t.description?'<p style="color:#8b98a9;font-size:14px;margin-top:10px">'+esc(t.description)+'</p>':'')+
        (l.project_code?'<pre>'+esc(l.project_code)+'</pre>':'')+'</div>';
  (t.exercises||[]).forEach(function(ex,i){
    h+='<div class="ex"><div class="q">Ejercicio '+(i+1)+'</div><pre>'+esc(ex.question)+'</pre>'+
       '<div class="h"><b>Pista:</b> '+esc(ex.hint)+'</div>'+
       '<textarea id="ta'+i+'" placeholder="Escribe tu codigo Python aqui..."></textarea>'+
       '<div class="row"><button class="btn" onclick="check('+lid+','+tid+','+i+')">Comprobar</button>'+
       '<button class="ghost" onclick="reveal('+lid+','+tid+','+i+')">Ver respuesta</button></div>'+
       '<div id="fb'+i+'"></div></div>';
  });
  h+='<div class="nav">';
  if(tid>0)h+='<button class="ghost" onclick="showTopic('+lid+','+(tid-1)+')">&#8592; Tema anterior</button>';
  h+='<button class="btn" onclick="afterTopic('+lid+','+tid+')">Marcar tema y continuar &#9654;</button></div>';
  document.getElementById('body').innerHTML=h;nav();hud();
  document.getElementById('body').scrollTop=0;
}

function norm(s){
  return String(s).replace(/\\s+/g,' ')
    .replace(/["']/g,'"')
    .replace(/\\bprint\\s*\\(/g,'print(')
    .replace(/\\)\\s*$/,'')
    .trim().toLowerCase();
}
function keywords(s){
  return String(s).replace(/["']/g,' ').replace(/[^a-zA-Z0-9_ ]/g,' ').split(/\\s+/).filter(function(w){return w.length>2;});
}

function check(lid,tid,i){
  var t=topicsOf(COURSE[lid])[tid],ex=t.exercises[i];
  var user=document.getElementById('ta'+i).value;
  var fb=document.getElementById('fb'+i);
  if(!user.trim()){fb.innerHTML='<div class="no">Escribe algo primero</div>';return;}
  var a=norm(ex.answer),b=norm(user);
  var kw=keywords(ex.answer),uw=keywords(user);
  var hit=kw.filter(function(w){return uw.indexOf(w)>-1;}).length;
  var good=(a===b)||(a.indexOf(b)===0&&b.length>6)||(hit>=Math.max(1,Math.ceil(kw.length*0.7)));
  if(good){
    fb.innerHTML='<div class="ok">&#10004; Correcto! +5 puntos</div>';
    var k=key(lid,tid);
    if(S.done.indexOf(k)===-1){S.done.push(k);S.score+=5;S.streak++;saveS();}
  }else{
    fb.innerHTML='<div class="no">&#10007; Casi. Revisa la pista e intentalo de nuevo.</div>';
  }
  nav();hud();
}

function reveal(lid,tid,i){
  var t=topicsOf(COURSE[lid])[tid],ex=t.exercises[i];
  document.getElementById('fb'+i).innerHTML='<div class="h" style="margin-top:10px"><b>Respuesta:</b></div><pre>'+esc(ex.answer)+'</pre>';
}

function afterTopic(lid,tid){
  var k=key(lid,tid);
  if(S.done.indexOf(k)===-1){S.done.push(k);S.score+=5;S.streak++;saveS();}
  var t=topicsOf(COURSE[lid]);
  if(tid+1<t.length){showTopic(lid,tid+1);return;}
  var ids=Object.keys(COURSE).sort(function(a,b){return a-b;});
  var p=ids.indexOf(String(lid));
  if(p>-1&&p+1<ids.length){showLesson(ids[p+1]);return;}
  showCert();
}

function showCert(){
  var it=allItems(),n=it.length,p=S.done.length;
  if(p<n){
    document.getElementById('ttl').textContent='Certificado';
    document.getElementById('body').innerHTML='<div class="cert"><h2>&#128942; Todavia no</h2><p>Completa los '+n+' temas para obtener tu certificado</p><p style="color:#22d3ee;font-size:22px;font-weight:700">'+p+' / '+n+' ('+Math.round(p/n*100)+'%)</p><div class="nav" style="justify-content:center"><button class="btn" onclick="nextTopic()">Continuar aprendiendo</button></div></div>';
    nav();hud();return;
  }
  document.getElementById('ttl').textContent='Certificado';
  var d=new Date().toLocaleDateString('es');
  document.getElementById('body').innerHTML='<div class="cert"><div style="font-size:56px">&#127942;</div><h2>Certificado de Finalizacion</h2><p>Se otorga a</p><h2 style="font-size:24px;color:#fff;margin:12px 0">&#128100; Crico719</h2><p>por completar el curso de <b style="color:#22d3ee">Python Learn</b></p><p>'+n+' temas &middot; 14 proyectos &middot; '+d+'</p><p style="margin-top:18px;font-size:12px">Puntaje final: '+S.score+' puntos</p><div class="nav" style="justify-content:center"><button class="ghost" onclick="resetAll()">Reiniciar progreso</button></div></div>';
  nav();hud();
}

function resetAll(){
  if(confirm('Borrar todo tu progreso?')){S={done:[],score:0,streak:0};saveS();goHome();}
}

loadS();goHome();
</script>
</body>
</html>
'''

# Build sections list from course
secs = []
cur = None
for i in range(1, 91):
    l = course.get(str(i))
    if not l:
        continue
    t = l.get('topics') or []
    title = t[0]['title'] if t else l['title']
    kind = 'project' if l.get('type') == 'PROJECT_GUIDED' else 'learn'
    if cur is None or cur['k'] != kind:
        cur = {'k': kind, 'n': title, 'ls': []}
        secs.append(cur)
    cur['ls'].append(str(i))

out = HTML.replace('__DATA__', data).replace('__SECS__', json.dumps(secs, ensure_ascii=False))

with open('web/index.html', 'w', encoding='utf-8') as f:
    f.write(out)
print('web/index.html generado:', len(out), 'chars,', len(course), 'lecciones,', len(secs), 'secciones')
