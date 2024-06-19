"use client"
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import ReactPaginate from 'react-paginate';
// import Footer from '../../components/Footer';
// import Loaders from '../../Loader';
import { Loader } from 'lucide-react';

interface Etudiant {
  matricule: string;
  // prenoms: string;
  // slug: string;
  // Bio: string;
}

const Etudiants: React.FC = () => {
  // const matricule = typeof window !== 'undefined' ? localStorage.getItem("matricule") : null;
  const [etudiants, setEtudiants] = useState<Etudiant[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [filteredEtudiants, setFilteredEtudiants] = useState<Etudiant[]>([]);
  const [pageSize, setPageSize] = useState<number>(10);
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(true);
  const [loads, setLoads] = useState<boolean>(true);

  const getEtudiants = async () => {
    setLoading(true);
    try {
      const response = await axios.get<Etudiant[]>(
        "http://127.0.0.1:8000/etudiants/"
      );
      setEtudiants(response.data);
      setFilteredEtudiants(response.data);
    } catch (error) {
      console.error("Erreur lors du chargement des étudiants :", error);
    }
    setLoading(false);
  };

  useEffect(() => {
    getEtudiants();
  }, []);

  useEffect(() => {
    const filtered = etudiants.filter(etudiant =>
      etudiant.matricule.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredEtudiants(filtered);
    setCurrentPage(0);
  }, [searchTerm, etudiants]);

  const itemsPerPage = pageSize;
  const offset = currentPage * itemsPerPage;
  const currentEtudiants = filteredEtudiants.slice(offset, offset + itemsPerPage);

  const handlePageSizeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const newSize = Number(event.target.value);
    setPageSize(newSize);
    setCurrentPage(0);
  };

  useEffect(() => {
    getEtudiants();
    setTimeout(() => {
      setLoads(false)
    }, 1000);
  }, []);

  return (
    <div>
      <div className={loads ? "" : "d-none"}>
        <Loader />
      </div>

      <div className={loads ? "d-none" : ""}>
        <div className="main-content">
          <section className="section">
            <div className="row">
              <div className="col-12 col-sm-12 col-lg-12">
                <div className="card ">
                  <div className="card-header">
                    <h4>Gestion des étudiants</h4>
                    <div className="card-header-action">
                      <div className="btn-group" style={{ height: "2.1rem" }}>
                        <Link href="/modifier-tâche">
                          <div className="d-flex btn btn-primary">
                            <span className="align-self-center">Modifier</span>
                          </div>
                        </Link>
                        <Link href="/assigner-tâche">
                          <div className="d-flex btn btn-success">
                            <span className="align-self-center">Ajouter</span>
                          </div>
                        </Link>
                      </div>
                    </div>
                  </div>
                  <div className="card-body">
                    <div className="row d-flex justify-content-between">
                      <div className="form-group col-4">
                        <span>Rechercher </span>
                        <div className="input-group mt-3">
                          <div className="input-group-prepend">
                            <div className="input-group-text">
                              <i className="fas fa-search"></i>
                            </div>
                          </div>
                          <input
                            type="text"
                            className="form-control"
                            placeholder="Rechercher par nom"
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                          />
                        </div>
                      </div>
                      <div className="form-group col-4">
                        <span>Affichage par page </span>
                        <div className="input-group mt-3">
                          <div className="input-group-prepend"></div>
                          <select
                            className="form-control"
                            value={pageSize}
                            onChange={handlePageSizeChange}
                          >
                            <option value={10}>10 par page</option>
                            <option value={20}>20 par page</option>
                            <option value={100}>100 par page</option>
                            <option value={filteredEtudiants.length}>Tout afficher</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    {loading ? (
                      <p className="text-center" style={{ color: 'green', fontSize: "24px" }}>Traitement...</p>
                    ) : filteredEtudiants.length === 0 ? (
                      <p className="text-center" style={{ color: 'red', fontSize: "24px" }}>Aucune donnée trouvée</p>
                    ) : (
                      <div className="table-responsive">
                        <table className="table table-striped" id="table-1">
                          <thead>
                            <tr>
                              <th className="text-center">#</th>
                              {/* <th>Nom</th>
                              <th>Prenom</th> */}
                              <th>Matricule</th>
                              {/* <th>Biographie</th> */}
                            </tr>
                          </thead>
                          <tbody>
                            {currentEtudiants.map((etudiant, index) => (
                              <tr key={index}>
                                <td>{offset + index + 1}</td>
                                <td>{etudiant.matricule}</td>
                                {/* <td>{etudiant.prenoms}</td>
                                <td>{etudiant.slug}</td>
                                <td>{etudiant.Bio}</td> */}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}
                    <ReactPaginate
                      previousLabel={<i className="fas fa-chevron-left"></i>}
                      nextLabel={<i className="fas fa-chevron-right"></i>}
                      pageCount={Math.ceil(filteredEtudiants.length / itemsPerPage)}
                      onPageChange={({ selected }) => setCurrentPage(selected)}
                      containerClassName={"pagination"}
                      activeClassName={"active"}
                      previousClassName={"pagination-btn"}
                      nextClassName={"pagination-btn"}
                      disabledClassName={"disabled"}
                      pageClassName={"page-item"}
                      pageLinkClassName={"page-link"}
                      breakClassName={"page-item"}
                      breakLinkClassName={"page-link"}
                      marginPagesDisplayed={1}
                      pageRangeDisplayed={3}
                    />
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
};

export default Etudiants;