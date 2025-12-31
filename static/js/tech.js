function showTechniques() {
    const stressLevel = document.getElementById('stressLevel').value;
    const techniquesContainer = document.getElementById('techniques');
    techniquesContainer.innerHTML = ''; // Clear previous techniques

    let techniques = '';

    if (stressLevel == '1') {
        techniques = `
            <div class="technique">
                <h3>Level 1 Stress Relief Techniques:</h3>
                <ul>
                    <li>Practice deep breathing exercises.</li>
                    <li>Take a short walk outside to clear your mind.</li>
                    <li>Listen to calming music for relaxation.</li>
                </ul>
            </div>
        `;
    } else if (stressLevel == '2') {
        techniques = `
            <div class="technique">
                <h3>Level 2 Stress Relief Techniques:</h3>
                <ul>
                    <li>Try progressive muscle relaxation techniques.</li>
                    <li>Engage in a hobby that helps you relax.</li>
                    <li>Write in a journal to express your feelings.</li>
                </ul>
            </div>
        `;
    } else if (stressLevel == '3') {
        techniques = `
            <div class="technique">
                <h3>Level 3 Stress Relief Techniques:</h3>
                <ul>
                    <li>Consider meditation or mindfulness practices.</li>
                    <li>Practice yoga or gentle stretches.</li>
                    <li>Talk to a counselor or therapist for support.</li>
                </ul>
            </div>
        `;
    } else {
        techniques = `<p>Please select a valid stress level to see the techniques.</p>`;
    }

    techniquesContainer.innerHTML = techniques;
}