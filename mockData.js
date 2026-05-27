const mockData = {
  parents: [
    {
      parentId: "P124556",
      addedOn: "25 Mar 2024",
      father: {
        name: "Rakesh Patel"
      },
      mother: {
        name: "Kavita Patel"
      },
      guardian: {
        type: "father", // 'father', 'mother', or 'other'
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
        name: "Anil Gupta"
      },
      mother: {
        name: "Sunita Gupta"
      },
      guardian: {
        type: "other",
        name: "Suresh Verma",
        email: "anil.gupta@example.com", // Keeping as per UI mock
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
        name: "Vikram Singh"
      },
      mother: {
        name: "Priya Singh"
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
        name: "Suresh Das"
      },
      mother: {
        name: "Meera Das"
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
        name: "Amit Reddy"
      },
      mother: {
        name: "Sneha Reddy"
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
        name: "Nitin Patel"
      },
      mother: {
        name: "Aarti Patel"
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

// If using ES6 modules in future
// export default mockData;
