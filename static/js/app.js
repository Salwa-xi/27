document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('http://localhost:5000');
    const patientList = document.getElementById("patient-list");

    socket.on('update_data', (patients) => {
        patientList.innerHTML = '';
        patients.forEach(patient => {
            const patientCard = `
                <div class="col-md-4">
                    <div class="card text-center p-3">
                        <div class="card-body">
                            <h5 class="card-title">${patient.name}</h5>
                            <p class="card-text">
                                Heart Rate: 
                                <strong class="text-success">${patient.heart_rate} BPM</strong>
                            </p>
                        </div>
                    </div>
                </div>
            `;
            patientList.innerHTML += patientCard;
        });
    });
});
