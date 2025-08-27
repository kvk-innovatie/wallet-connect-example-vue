import express from 'express';
import axios from 'axios';

const app = express();

app.use(express.json());

// Proxy endpoint for disclosed attributes
app.get('/api/disclosed-attributes*', async (req, res) => {
  const apiKey = 'ee1c64c4e3d2f6bb1f9f0f4b9cabdffac1391966456e2e59760194b3478b2bad';
  
  try {
    const response = await axios({
      method: req.method,
      url: `https://wallet-connect.eu${req.url}`,
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
    });
    
    res.status(response.status).json(response.data);
  } catch (error) {
    if (error.response) {
      res.status(error.response.status).json(error.response.data);
    } else {
      res.status(500).json({ error: 'Proxy error', message: error.message });
    }
  }
});

app.listen(4000, () => {
  console.log('Node.js backend running on port 4000');
});