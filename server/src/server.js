import express from 'express';
import cors from 'cors';
import morgan from 'morgan';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { spawn } from 'child_process';

// Configuración de variables de entorno
dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(cors());
app.use(morgan('dev'));
app.use(express.json());

// Servicio para ejecutar scripts de Python
const pythonService = {
    runScript: (scriptName, args = []) => {
        return new Promise((resolve, reject) => {
            const pythonProcess = spawn('python3', [
                join(__dirname, '../game_engine', scriptName),
                ...args
            ]);

            let data = '';
            let error = '';

            pythonProcess.stdout.on('data', (chunk) => {
                data += chunk.toString();
            });

            pythonProcess.stderr.on('data', (chunk) => {
                error += chunk.toString();
            });

            pythonProcess.on('close', (code) => {
                if (code !== 0) {
                    reject(new Error(`Python script exited with code ${code}: ${error}`));
                    return;
                }
                try {
                    const result = JSON.parse(data);
                    resolve(result);
                } catch (e) {
                    reject(new Error(`Failed to parse Python output: ${e.message}`));
                }
            });
        });
    }
};

// Endpoints del juego
app.post('/api/blackjack/start', async (req, res) => {
    try {
        const result = await pythonService.runScript('blackjack.py', ['start']);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/blackjack/hit', async (req, res) => {
    try {
        const { playerId } = req.body;
        const result = await pythonService.runScript('blackjack.py', ['hit', playerId]);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/blackjack/stand', async (req, res) => {
    try {
        const { playerId } = req.body;
        const result = await pythonService.runScript('blackjack.py', ['stand', playerId]);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/api/blackjack/bet', async (req, res) => {
    try {
        const { playerId, amount } = req.body;
        const result = await pythonService.runScript('blackjack.py', ['bet', playerId, amount]);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
