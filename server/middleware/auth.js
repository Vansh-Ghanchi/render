const authRole = (...role) => {
    return (req, res, next) => {
        if (!role.includes(req.user.role)) {
            res.status(404).json({ msg: "Acces denailed : autorization failed" })
        }
        next()
    }
}

module.exports = authRole