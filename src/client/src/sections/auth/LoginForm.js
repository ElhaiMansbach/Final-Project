import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../components/iconify/Iconify';

export default function LoginForm() {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);
  const [id, setId] = useState('');
  const [password, setPassword] = useState('');

  // const handleClick = () => {
  //   navigate('/peoples_budget/home', { replace: true });
  // };

  const handleClick = async () => {
    const url = 'http://localhost:3000/peoples_budget/login';
    // const data = { id, password };

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: 'john', password: 'doe' })
      });

      const responseData = await response.json();
      console.log(responseData);

    }
    catch (e) { console.log(e, "something") }

    navigate('/peoples_budget/home', { replace: true });
  }


  return (
    <>
      <Stack spacing={3}>
        <TextField id="id" label="ID" value={id} onChange={(e) => setId(e.target.value)} />

        <TextField
          id="password"
          label="Password"
          type={showPassword ? 'text' : 'password'}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
      </Stack>

      <Stack direction="row" alignItems="center" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Link variant="subtitle2" underline="none" color="black" alignItems="left">
          Remember me
        </Link>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={handleClick}>
        Login
      </LoadingButton>
    </>
  );
}