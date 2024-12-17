// script.js
document.getElementById('predictButton').addEventListener('click', async function () {
    const data = {
        Age: parseInt(document.getElementById('age').value),
        Department: parseInt(document.getElementById('department').value),
        MonthlyIncome: parseInt(document.getElementById('income').value),
        JobSatisfaction: parseInt(document.getElementById('satisfaction').value),
        YearsAtCompany: parseInt(document.getElementById('experience').value)
    };

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.attrition_risk
        ? "High Risk of Attrition"
        : "Low Risk of Attrition";
});

// Fetch and display employee summary
async function loadEmployeeSummary() {
    const response = await fetch('http://127.0.0.1:5000/employee_summary');
    const summary = await response.json();

    document.getElementById('summary').innerHTML = `
        <p>Total Employees: ${summary.total_employees}</p>
        <p>Employees who left: ${summary.employees_left}</p>
        <p>Attrition Rate: ${summary.attrition_rate}%</p>
    `;
}

// Load summary when the page is loaded
window.onload = loadEmployeeSummary;


// // script.js
// document.getElementById('predictButton').addEventListener('click', async function () {
//     const data = {
//         Age: parseInt(document.getElementById('age').value),
//         Department: parseInt(document.getElementById('department').value),
//         MonthlyIncome: parseInt(document.getElementById('income').value),
//         JobSatisfaction: parseInt(document.getElementById('satisfaction').value),
//         YearsAtCompany: parseInt(document.getElementById('experience').value)
//     };

//     const response = await fetch('http://127.0.0.1:5000/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     });

//     const result = await response.json();
//     document.getElementById('result').innerText = result.attrition_risk
//         ? "High Risk of Attrition"
//         : "Low Risk of Attrition";
// });
