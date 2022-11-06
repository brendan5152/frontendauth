import Events from '../../models/userModel';
import connectDB from './auth/lib/connectDB';

connectDB()

export default async function handler(req, res) {
    
    const body = req.body
    console.log(body)
    const { method } = req;
    switch (method) {
        case 'GET':
            // Get data from your database
            res.status(200).json({method: 'GET', endpoint: 'events'})
            break
        case 'POST':
            // Update or create data in your database
            res.status(200).json({method: 'POST', endpoint:'events'})
            break
        default:
            res.setHeader('Allow', ['GET', 'POST'])
            res.status(405).end(`Method ${method} Not Allowed`)
    }
}