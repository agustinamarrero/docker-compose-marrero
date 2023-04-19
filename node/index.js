import axios from 'axios';
import express from 'express';

const app = express()
const port = 80



app.get('/ping', (req, res) => {
  const serverName = 'Servidor 1 ';
  res.status(200).json({ message: 'Pong!' });
})

app.get('/forward', async (req, res) => {
  try {
    const url = req.query.url;
    const response = await axios.get(url);
    res.status(200).json(response.data);
  } catch (e) {
    res.status(500).send({ "message": "error getting data from external service" })
  }
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})


