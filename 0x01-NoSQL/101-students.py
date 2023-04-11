#!/usr/bin/env python3
""" Script returns average score of students """


def top_students(mongo_collection):
    
    """ Returns all students sorted by average score """
    best_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return best_student
