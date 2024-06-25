
<<<<<<< HEAD
=======
export type Employee = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  gender: string;
  date_of_birth: string; // Consider using a proper date type if possible
  street: string;
  city: string;
  state: string;
  country: string;
  zipcode: string;
  longitude?: number; // Optional field
  latitude?: number; // Optional field
  job: string;
  profile_picture?: string | null; // Profile picture can be a string (URL) or null (if no picture)
};
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997

export type Etudiant = {
  id: number;
  username: string;
  nom: string;
  prenom: string;
  filiere_id: number;
  annee_id: number;
  email: string;
  biographie: string;
};
<<<<<<< HEAD
export type Enseignant = {
  id: number;
  username: string;
  nom: string;
  prenom: string;
  departement_id: number;
  grade_id: number;
  annee_id: number;
  email: string;
  biographie: string;
};
=======
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
