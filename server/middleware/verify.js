const dotenv = require('dotenv');
dotenv.config();
const jwt = require("jsonwebtoken");
const verfiy = (req, res, next) => {
    const token = req.cookies.token;
    if (!token) {
        return res.status(401).json({ message: 'Unauthorized' });
    }
    try {
        const decoded = jwt.verify(token,process.env.JWT_SECRET)
        if(decoded){
            // res.redirect('/home')
            req.user = decoded;
            next();
        }
    } catch (error) {
        // return res.status(404).json({ error: error.message });
        res.redirect('/login')
    }
}
module.exports =verfiy;
