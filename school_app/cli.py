import argparse
import uuid
from data import load_data, save_data


def add_student(args):
    data = load_data()
    student = {
        "id": str(uuid.uuid4()),
        "name": args.name,
        "age": args.age,
        "courses": [],
    }
    data["students"].append(student)
    save_data(data)
    print(f"Added student {args.name}")


def list_students(args):
    data = load_data()
    for s in data["students"]:
        print(f"{s['id']}: {s['name']} ({s['age']})")


def edit_student(args):
    data = load_data()
    for s in data["students"]:
        if s["id"] == args.id:
            if args.name:
                s["name"] = args.name
            if args.age is not None:
                s["age"] = args.age
            break
    save_data(data)
    print(f"Updated student {args.id}")


def add_teacher(args):
    data = load_data()
    teacher = {
        "id": str(uuid.uuid4()),
        "name": args.name,
        "courses": [],
    }
    data["teachers"].append(teacher)
    save_data(data)
    print(f"Added teacher {args.name}")


def list_teachers(args):
    data = load_data()
    for t in data["teachers"]:
        print(f"{t['id']}: {t['name']}")


def edit_teacher(args):
    data = load_data()
    for t in data["teachers"]:
        if t["id"] == args.id:
            if args.name:
                t["name"] = args.name
            break
    save_data(data)
    print(f"Updated teacher {args.id}")


def add_course(args):
    data = load_data()
    course = {
        "id": str(uuid.uuid4()),
        "name": args.name,
        "teacher": args.teacher,
    }
    data["courses"].append(course)
    save_data(data)
    print(f"Added course {args.name}")


def list_courses(args):
    data = load_data()
    for c in data["courses"]:
        print(f"{c['id']}: {c['name']} (teacher {c['teacher']})")


def edit_course(args):
    data = load_data()
    for c in data["courses"]:
        if c["id"] == args.id:
            if args.name:
                c["name"] = args.name
            if args.teacher:
                c["teacher"] = args.teacher
            break
    save_data(data)
    print(f"Updated course {args.id}")


def delete_entry(args):
    data = load_data()
    collection = data[args.category]
    data[args.category] = [item for item in collection if item['id'] != args.id]
    save_data(data)
    print(f"Deleted {args.id} from {args.category}")


def get_parser():
    parser = argparse.ArgumentParser(description="School App CLI")
    subparsers = parser.add_subparsers(dest="command")

    s_add = subparsers.add_parser("add_student")
    s_add.add_argument("name")
    s_add.add_argument("age", type=int)
    s_add.set_defaults(func=add_student)

    s_list = subparsers.add_parser("list_students")
    s_list.set_defaults(func=list_students)

    s_edit = subparsers.add_parser("edit_student")
    s_edit.add_argument("id")
    s_edit.add_argument("name", nargs="?")
    s_edit.add_argument("age", type=int, nargs="?")
    s_edit.set_defaults(func=edit_student)

    t_add = subparsers.add_parser("add_teacher")
    t_add.add_argument("name")
    t_add.set_defaults(func=add_teacher)

    t_list = subparsers.add_parser("list_teachers")
    t_list.set_defaults(func=list_teachers)

    t_edit = subparsers.add_parser("edit_teacher")
    t_edit.add_argument("id")
    t_edit.add_argument("name", nargs="?")
    t_edit.set_defaults(func=edit_teacher)

    c_add = subparsers.add_parser("add_course")
    c_add.add_argument("name")
    c_add.add_argument("teacher")
    c_add.set_defaults(func=add_course)

    c_list = subparsers.add_parser("list_courses")
    c_list.set_defaults(func=list_courses)

    c_edit = subparsers.add_parser("edit_course")
    c_edit.add_argument("id")
    c_edit.add_argument("name", nargs="?")
    c_edit.add_argument("teacher", nargs="?")
    c_edit.set_defaults(func=edit_course)

    delete = subparsers.add_parser("delete")
    delete.add_argument("category", choices=["students", "teachers", "courses"])
    delete.add_argument("id")
    delete.set_defaults(func=delete_entry)

    return parser


def main(argv=None):
    parser = get_parser()
    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

