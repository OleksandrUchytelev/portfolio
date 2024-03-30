let isAnimating = true;

function stopAnimation() {
    const jsSkill = document.getElementById('jsSkill');
    jsSkill.style.animationPlayState = 'paused';
    isAnimating = false;
}

function startAnimation() {
    const jsSkill = document.getElementById('jsSkill');
    jsSkill.style.animationPlayState = 'running';
    isAnimating = true;
}

startAnimation();

const jsSkill = document.getElementById('jsSkill');
jsSkill.addEventListener('click', function() {
    if (isAnimating) {
        stopAnimation();
    } else {
        startAnimation();
    }
});
