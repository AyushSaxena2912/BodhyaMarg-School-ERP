const mockData = {
  parents: [
    {
      parentId: "P124556",
      addedOn: "25 Mar 2024",
      father: {
        name: "Rakesh Patel",
        email: "rakesh@example.com",
        phone: "+91 91234 56789"
      },
      mother: {
        name: "Kavita Patel",
        email: "kavita@example.com",
        phone: "+91 99887 76655"
      },
      guardian: {
        type: "father",
        name: "Rakesh Patel",
        email: "rakesh@example.com",
        phone: "+91 91234 56789",
        relation: "Father"
      },
      children: [
        { name: "Ananya Patel", class: "III, A", rollNo: "35013", gender: "Female", dateJoined: "22 Mar 2018", status: "Active", admissionNo: "AD9892434" },
        { name: "Aryan Patel", class: "I, B", rollNo: "35012", gender: "Male", dateJoined: "18 Mar 2018", status: "Active", admissionNo: "AD9892433" }
      ]
    },
    {
      parentId: "P124555",
      addedOn: "18 Mar 2024",
      father: {
        name: "Anil Gupta",
        email: "anil.dad@example.com",
        phone: "+91 91111 22222"
      },
      mother: {
        name: "Sunita Gupta",
        email: "sunita.mom@example.com",
        phone: "+91 92222 33333"
      },
      guardian: {
        type: "other",
        name: "Suresh Verma",
        email: "anil.gupta@example.com",
        phone: "+91 99887 76655",
        relation: "Uncle"
      },
      children: [
        { name: "Vivaan Gupta", class: "V, C", rollNo: "45021", gender: "Male", dateJoined: "10 Apr 2019", status: "Active", admissionNo: "AD9892435" }
      ]
    },
    {
      parentId: "P124554",
      addedOn: "14 Mar 2024",
      father: {
        name: "Vikram Singh",
        email: "vikram@example.com",
        phone: "+91 93333 44444"
      },
      mother: {
        name: "Priya Singh",
        email: "priya.s@example.com",
        phone: "+91 88776 65544"
      },
      guardian: {
        type: "mother",
        name: "Priya Singh",
        email: "priya.s@example.com",
        phone: "+91 88776 65544",
        relation: "Mother"
      },
      children: [
        { name: "Diya Singh", class: "II, A", rollNo: "25010", gender: "Female", dateJoined: "05 Jun 2020", status: "Active", admissionNo: "AD9892436" }
      ]
    },
    {
      parentId: "P124553",
      addedOn: "27 Feb 2024",
      father: {
        name: "Suresh Das",
        email: "suresh.father@example.com",
        phone: "+91 94444 55555"
      },
      mother: {
        name: "Meera Das",
        email: "meera.mom@example.com",
        phone: "+91 95555 66666"
      },
      guardian: {
        type: "other",
        name: "Prakash Das",
        email: "suresh.d@example.com",
        phone: "+91 77665 54433",
        relation: "Uncle"
      },
      children: [
        { name: "Kabir Das", class: "IV, B", rollNo: "45012", gender: "Male", dateJoined: "12 Apr 2021", status: "Active", admissionNo: "AD9892437" }
      ]
    },
    {
      parentId: "P124552",
      addedOn: "11 Feb 2024",
      father: {
        name: "Amit Reddy",
        email: "amit.reddy@example.com",
        phone: "+91 99001 12233"
      },
      mother: {
        name: "Sneha Reddy",
        email: "sneha.reddy@example.com",
        phone: "+91 96666 77777"
      },
      guardian: {
        type: "father",
        name: "Amit Reddy",
        email: "amit.reddy@example.com",
        phone: "+91 99001 12233",
        relation: "Father"
      },
      children: [
        { name: "Myra Reddy", class: "II, B", rollNo: "25018", gender: "Female", dateJoined: "01 Jul 2022", status: "Active", admissionNo: "AD9892438" }
      ]
    },
    {
      parentId: "P124551",
      addedOn: "24 Jan 2024",
      father: {
        name: "Nitin Patel",
        email: "nitin.dad@example.com",
        phone: "+91 97777 88888"
      },
      mother: {
        name: "Aarti Patel",
        email: "nitin.patel@example.com",
        phone: "+91 88990 01122"
      },
      guardian: {
        type: "mother",
        name: "Aarti Patel",
        email: "nitin.patel@example.com",
        phone: "+91 88990 01122",
        relation: "Mother"
      },
      children: [
        { name: "Aarav Patel", class: "VI, A", rollNo: "65005", gender: "Male", dateJoined: "15 May 2017", status: "Active", admissionNo: "AD9892439" }
      ]
    }
  ]
};
