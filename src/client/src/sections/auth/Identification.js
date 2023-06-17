import { useState } from 'react';
import { Stack, Button, TextField, Typography } from '@mui/material';
import PropTypes from 'prop-types';


export default function Identification(props) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [id, setId] = useState('');
  const [birthDate, setBirthDate] = useState('');

  const [firstNameError, setFirstNameError] = useState('');
  const [lastNameError, setLastNameError] = useState('');
  const [idError, setIdError] = useState('');
  const [birthDateError, setBirthDateError] = useState('');

  // Makes sure there are only words in the name
  const nameRegex = /^[\p{L}]+$/u;

  const dob = new Date(birthDate);
  const today = new Date();
  let age = today.getFullYear() - dob.getFullYear();
  const monthDiff = today.getMonth() - dob.getMonth();

  const handleSubmit = async () => {
    const url = 'http://localhost:5000/peoples_budget/forget_password';

    // Validate the input fields
    if (firstName.length <= 2) {
      setFirstNameError('Invalid First name: Please enter a first name.');
      return;
    }
    setFirstNameError('');

    if (!nameRegex.test(firstName)) {
      setFirstNameError('Invalid First name: Please enter a valid name without numbers or special characters.');
      return;
    }
    setFirstNameError('');

    if (lastName.length <= 2) {
      setLastNameError('Invalid Last name: Please enter a last name.');
      return;
    }
    setLastNameError('');

    if (!nameRegex.test(lastName)) {
      setLastNameError('Invalid Last name: Please enter a valid name without numbers or special characters.');
      return;
    }
    setLastNameError('');

    if (id.length !== 9) {
      setIdError('Invalid ID: Please enter a 9 digit number.');
      return;
    }
    setIdError('');

    if (id === '000000000') {
      setIdError('Invalid ID: This ID belongs to guest user.');
      return;
    }
    setIdError('');

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
      age -= 1;
    }

    if (age < 18) {
      setBirthDateError('Invalid Birth Date: You are under 18 - you can not sign up.');
      return;
    }
    setBirthDateError('');

    if (age > 120) {
      setBirthDateError('Invalid Birth Date: You are over 120 years old.');
      return;
    }
    setBirthDateError('');

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ firstName, lastName, id, birthDate }),
      });

      const responseData = await response.json();
      if (responseData.status === 'Succeeded') {
        props.setIsShowed(false);
      } else if (responseData.status === 'Invalid first name') {
        setFirstNameError('Invalid First Name: Not recognized in the system.');
      } else if (responseData.status === 'Invalid last name') {
        setLastNameError('Invalid Last Name: Not recognized in the system.');
      } else if (responseData.status === 'Invalid id') {
        setLastNameError('Invalid ID: Not recognized in the system.');
      } else if (responseData.status === 'Invalid birth date') {
        setLastNameError('Invalid Birth Date: Not recognized in the system.');
      } else {
        throw new Error('Error!, Please try again');
      }
    } catch (error) {
      console.error(error);
      alert('An error was received, please refresh the page and try again');
    }
  };

  return (
    <>
      <Typography variant="h4" gutterBottom sx={{ marginTop: '-48px', display: 'flex', justifyContent: 'center' }}>
        Forget Password ?
      </Typography>
      <Stack spacing={2}>
        <TextField
          id="fName"
          label="First name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          error={Boolean(firstNameError)}
          helperText={firstNameError}
        />
        <TextField
          id="lName"
          label="Last name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          error={Boolean(lastNameError)}
          helperText={lastNameError}
        />
        <TextField
          id="signId"
          label="ID"
          value={id}
          onChange={(e) => setId(e.target.value)}
          error={Boolean(idError)}
          helperText={idError}
        />
        <TextField
          id="date"
          label="Birth Date"
          type="date"
          value={birthDate}
          onChange={(e) => setBirthDate(e.target.value)}
          defaultValue="yyyy-MM-dd"
          error={Boolean(birthDateError)}
          helperText={birthDateError}
          InputLabelProps={{
            shrink: true,
          }}
        />
      </Stack>

      <Stack sx={{ marginTop: 2 }}>
        <Button
          id="submitBtn"
          fullWidth
          size="large"
          type="submit"
          variant="contained"
          sx={{ fontSize: '1rem' }}
          onClick={handleSubmit}
        >
          Submit
        </Button>
      </Stack>
    </>
  );
}

Identification.propTypes = {
  setIsShowed: PropTypes.func.isRequired,
};