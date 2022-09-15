#include "lists.h"
#include "stdlib.h"
/**
 *insert_node - inserts a node in a sorted singly linked lis
 *
 *@head: a pointer to the head pointer of the list
 *@number: the number to set s value of new node
 *Return: the address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node)
	{
		new_node->n = number;
		if (*head == NULL)
		{
			new_node->next = NULL;
			*head = new_node;
			return (new_node);
		}
		current = *head;
		while (current && (number > current->n))
		{
			prev = current;
			current = current->next;
		}
		new_node->next = current;
		prev->next = new_node;
		return (new_node);
	}
	return (NULL);
}
