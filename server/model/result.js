const mongoose = require('mongoose');
const resultSchema = new mongoose.Schema({
    studentId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Student',
        required: true
    },
    sem: {
        type: Number,
        required: true
    },
    subjects: [
        {
            subject: {
                type: String,
                required: true
            },
            marks: {
                type: Number,
                required: true
            }
        }
    ],
    total: {
        type: Number,
    },
    percentage: {
        type: Number,

    },
    CGPA: { type: Number },
    creditsEarned: { type: Number },
    resultStatus: { type: String }
}, { timestamps: true });

module.exports = mongoose.model('Result', resultSchema);