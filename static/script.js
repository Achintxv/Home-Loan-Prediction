// Sliders
const incomeRange = document.getElementById('incomeRange');
const tenureRange = document.getElementById('tenureRange');
const interestRange = document.getElementById('interestRange');
const otherEmiRange = document.getElementById('otherEmiRange');

// Slider Labels
const incomeValue = document.getElementById('incomeValue');
const tenureValue = document.getElementById('tenureValue');
const interestValue = document.getElementById('interestValue');
const otherEmiValue = document.getElementById('otherEmiValue');

// Extra Inputs
const creditScoreInput = document.getElementById('creditScore');
const ageInput = document.getElementById('age');
const employmentTypeSelect = document.getElementById('employmentType');

// Results
const eligibilityDisplay = document.getElementById('loanEligibility');
const emiDisplay = document.getElementById('loanEmi');

function updateSliderLabels() {
  incomeValue.value = `₹ ${parseInt(incomeRange.value).toLocaleString()}`;
  tenureValue.value = `${tenureRange.value}`;
  interestValue.value = `${interestRange.value}%`;
  otherEmiValue.value = `₹ ${parseInt(otherEmiRange.value).toLocaleString()}`;
}

function sendPredictionRequest() {
  const income = parseInt(incomeRange.value);
  const tenure = parseInt(tenureRange.value);
  const interestRate = parseFloat(interestRange.value);
  const otherEmi = parseInt(otherEmiRange.value);
  const creditScore = parseInt(creditScoreInput.value);
  const age = parseInt(ageInput.value);
  const employmentType = employmentTypeSelect.value;

  if (isNaN(creditScore) || isNaN(age) || employmentType === '') {
    console.warn("Fill in Credit Score, Age, and Employment Type!");
    return;
  }

  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      gross_income: income,
      tenure: tenure,
      interest_rate: interestRate,
      other_emis: otherEmi,
      credit_score: creditScore,
      age: age,
      employment_type: employmentType
    })
  })
  .then(response => response.json())
  .then(data => {
    eligibilityDisplay.innerText = `${parseInt(data.loan_amount).toLocaleString()}`;
    emiDisplay.innerText = data.emi ? `${parseInt(data.emi).toLocaleString()}` : '-';
  })
  .catch(error => console.error('Error:', error));
}

function handleInputChange() {
  updateSliderLabels();
  sendPredictionRequest();
}

[incomeRange, tenureRange, interestRange, otherEmiRange].forEach(slider => {
  slider.addEventListener('input', handleInputChange);
});

[creditScoreInput, ageInput, employmentTypeSelect].forEach(input => {
  input.addEventListener('input', handleInputChange);
});

// Init
updateSliderLabels();
