const DATA_URL = 'course.json';
let course = {};
let currentLesson = null;
let scores = {completed_topics: [], total_score: 0, streak: 0};

async function init() {
    const res = await fetch(DATA_URL);
    course = await res.json();
    loadScores();
    renderLessonList();
    updateStats();
}

function loadScores() {
    try {
        const s = localStorage.getItem('python_learn_scores');
        if (s) scores = JSON.parse(s);
    } catch(e) {}
}

function saveScores() {
    localStorage.setItem('python_learn_scores', JSON.stringify(scores));
}

function renderLessonList() {
    const list = document.getElementById('lessonList');
    list.innerHTML = '';
    const lessonIds = Object.keys(course).sort((a,b) => parseInt(a)-parseInt(b));
    lessonIds.forEach(lid => {
        const l = course[lid];
        const tps = l.topics || [{title: l.title, exercises: l.exercises || []}];
        const allDone = tps.every((_, i) => scores.completed_topics.includes(lid+'_'+i));
        const div = document.createElement('div');
        div.className = 'lesson-item' + (allDone ? ' completed' : '');
        let badges = '';
        tps.forEach((t, i) => {
            const done = scores.completed_topics.includes(lid+'_'+i);
            badges += '<span class=lesson-badge badge-' + (l.type||'learn') + '>' + (done?'✓':'') + '</span>';
        });
        div.innerHTML = '<div class=lesson-num>Leccion ' + lid + '</div><div class=lesson-name>' + l.title + '</div>' + badges;
        div.onclick = () => showLesson(lid);
        list.appendChild(div);
    });
}

function updateStats() {
    const done = scores.completed_topics.length;
    let total = 0;
    Object.values(course).forEach(l => { total += (l.topics || l.exercises || []).length; });
    document.getElementById('score').textContent = scores.total_score;
    document.getElementById('streak').textContent = scores.streak;
    document.getElementById('progress').textContent = done + '/' + total;
}

async function startCourse() {
    document.getElementById('hero').style.display = 'none';
    document.getElementById('lessonView').style.display = 'block';
    renderLessonList();
}

function goBack() {
    document.getElementById('hero').style.display = 'flex';
    document.getElementById('lessonView').style.display = 'block';
    document.getElementById('lessonDetail').style.display = 'none';
    document.getElementById('lessonsGrid').style.display = 'grid';
    currentLesson = null;
}

async function showLesson(lid) {
    currentLesson = lid;
    const l = course[lid];
    document.getElementById('lessonTitle').textContent = l.title;
    document.getElementById('lessonsGrid').style.display = 'grid';
    document.getElementById('lessonDetail').style.display = 'none';
    const grid = document.getElementById('lessonsGrid');
    grid.innerHTML = '';
    const tps = l.topics || [{title: l.title, exercises: l.exercises || []}];
    tps.forEach((t, i) => {
        const done = scores.completed_topics.includes(lid+'_'+i);
        const card = document.createElement('div');
        card.className = 'lesson-grid-item' + (done ? ' completed' : '');
        card.innerHTML = '<div class=num>' + (done?'✓':'') + '</div><div class=name>' + t.title + '</div>';
        card.onclick = () => showTopic(lid, i);
        grid.appendChild(card);
    });
    const doneCount = scores.completed_topics.filter(k=>k.startsWith(lid+'_')).length;
    document.getElementById('progressFill').style.width = (doneCount / tps.length * 100) + '%';
}

async function showTopic(lid, tid) {
    currentLesson = lid;
    const l = course[lid];
    const tps = l.topics || [{title: l.title, exercises: l.exercises || []}];
    const topic = tps[tid];
    const detail = document.getElementById('lessonDetail');
    detail.style.display = 'block';
    document.getElementById('lessonsGrid').style.display = 'none';
    let html = '<div class=topic-card><div class=topic-title>' + topic.title + '</div><div class=topic-desc>' + (topic.description||'') + '</div>';
    (topic.exercises || []).forEach((ex, i) => {
        html += '<div class=exercise><div class=exercise-title>' + (i+1) + '. ' + ex.question + '</div><textarea class=code-input id=code_' + lid + '_' + tid + '_' + i + ' placeholder="Escribe tu codigo aqui..."></textarea><button class=btn-run onclick=runCode(' + lid + ',' + tid + ',' + i + ')'>Ejecutar</button><div id=result_' + lid + '_' + tid + '_' + i + '></div></div>';
    });
    html += '</div>';
    detail.innerHTML = html;
}

function runCode(lid, tid, i) {
    const code = document.getElementById('code_' + lid + '_' + tid + '_' + i).value;
    const resultDiv = document.getElementById('result_' + lid + '_' + tid + '_' + i);
    if (!code.trim()) { resultDiv.innerHTML = '<div class=result-error>Escribe codigo primero</div>'; return; }
    try {
        eval(code);
        resultDiv.innerHTML = '<div class=result-ok>&#10003; Correcto!</div>';
        const key = lid + '_' + tid;
        if (!scores.completed_topics.includes(key)) {
            scores.completed_topics.push(key);
            scores.streak++;
            scores.total_score += 5;
            saveScores();
            updateStats();
            renderLessonList();
            showTopic(lid, tid);
        }
    } catch(e) {
        resultDiv.innerHTML = '<div class=result-error>&#10007; Error: ' + e.message + '</div>';
    }
}

init();
