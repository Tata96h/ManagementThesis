"use client";
import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Modal } from "@/components/ui/modal";

interface AlertModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
  loading: boolean;
}

export const AlertModal: React.FC<AlertModalProps> = ({
  isOpen,
  onClose,
  onConfirm,
  loading,
}) => {
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (!isMounted) {
    return null;
  }

  return (
    <Modal
<<<<<<< HEAD
      title="Etes-vous sûre?"
      description="Voulez-vous vraiment effectuer cette action?"
=======
      title="Are you sure?"
      description="This action cannot be undone."
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
      isOpen={isOpen}
      onClose={onClose}
    >
      <div className="pt-6 space-x-2 flex items-center justify-end w-full">
        <Button disabled={loading} variant="outline" onClick={onClose}>
<<<<<<< HEAD
          Annuler
        </Button>
        <Button disabled={loading} variant="destructive" onClick={onConfirm}>
          Supprimer
=======
          Cancel
        </Button>
        <Button disabled={loading} variant="destructive" onClick={onConfirm}>
          Continue
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
        </Button>
      </div>
    </Modal>
  );
};
